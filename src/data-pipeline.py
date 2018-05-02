from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from metadata_dict import country_names, event_names
from operator import itemgetter
import pyspark_cassandra

sc = SparkContext()
sqlContext = SQLContext(sc)
rdd = sc.textFile("s3a://kv-data/*")
rdd.cache()


# Discard records with missing/null information
def is_valid_record(record):
    try:
        int(record[1])
        int(record[4])
        float(record[5])
        float(record[6])
        return True
    except ValueError:
        return False

def get_event_code(record):
    if record[2] == "" and record[3] != "":
        return ((record[0], record[1], record[3], record[4], record[5], record[6]))
    else:
        return ((record[0], record[1], record[2], record[4], record[5], record[6]))

def popular_avg(curr_tup):
    #finds the most populat averages in dictionary of events
    lst = curr_tup[1]
    dictionary = curr_tup[2]
    dict_matches = {}
    for tup in lst:
        event_type = tup[0]
        dict_matches[event_type] = dictionary[event_type]
    return ((curr_tup[0], lst, dict_matches, curr_tup[3]))

def add_total(tup):
    #updates dictionary in tuple and adds new key and value
    main_dict = tup[1]
    info_dict = tup[2]
    for key in info_dict:
        main_dict[key].update(info_dict[key])
        main_dict["TotalArticles"] = {"total":tup[3]}
    return ((tup[0], main_dict))

def event_mentions(tup):
    #adding new key value to dicitonary for each event
    #this value represents the total number of times each
    #event was mentioned in other news sources
    lst = tup[1]
    dict_matches = {}
    for event_tup in lst:
        dict_matches[event_tup[0]] = {"ArticleMentions":event_tup[1]}
    return ((tup[0], dict_matches, tup[2], tup[3]))

def add_events(tup):
    #find the total sum of all the events for a country
    type_lst = tup[1]
    total_mentions = 0
    for event in type_lst:
        total_mentions += event[1]
    return ((tup[0], type_lst, tup[2], total_mentions))


def ingest_data(rdd):
    # Column indices
    time = 1
    actor1Type1Code = 12
    actor2Type1Code = 22
    numArticles = 33
    goldsteinScale = 30
    avgTone = 34
    actionGeo_CountryCode = 51

    gdelt_data  = rdd.map(lambda x: x.split('\t')) \
    	             .map(lambda x: ((x[actionGeo_CountryCode],
                            		    x[time],
                            		    x[actor1Type1Code],
                            		    x[actor2Type1Code],
                            		    x[numArticles],
                            		    x[goldsteinScale],
                            		    x[avgTone]))) \
    	             .filter(is_valid_record) \
    	             .map(lambda x: ((x[0],int(x[1]), x[2], x[3], int(x[4]), int(float(x[5])), int(float(x[6]))))) \
    	             .map(get_event_code) \
                     .filter(lambda x: x[0] in country_names and x[2] in event_names ) \
                     .map(lambda x: ((country_names[x[0]], x[1], event_names[x[2]], x[3], x[4], x[5]))) \
                     .map(lambda x: (((x[0], x[1], x[2]), (x[3],x[4],x[5],1)))) \
    	             .reduceByKey(lambda x,y: (x[0]+y[0], x[1]+y[1], x[2]+y[2], x[3]+y[3])) \
    	             .map(lambda x: ((x[0], (x[1][0], x[1][1]/x[1][3], x[1][2]/x[1][3]))))


    agg_data = gdelt_data.map(lambda t:((t[0][0],t[0][1]),
                                      ([(t[0][2],t[1][0])], [(t[0][2],{"goldstein_avg":t[1][1], "tone_avg":t[1][2]})]))) \
		                 .reduceByKey(lambda x, y: (x[0]+y[0], x[1]+y[1])) \
		                 .map(lambda v: (v[0], sorted(v[1][0], key=itemgetter(1), reverse=True), v[1][1])) \
		                 .map(add_events) \
                         .map(lambda f: ((f[0], f[1][:5], dict(f[2]), f[3]))) \
                         .map(popular_avg) \
		                 .map(event_mentions) \
                         .map(add_total) \
		                 .map(lambda d: ((d[0][0],d[0][1],d[1])))
    return agg_data

daily_data = ingest_data(rdd,"daily")
daily_rdd.saveToCassandra("gdelt","daily")
