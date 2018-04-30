from pyspark.sql import SparkSession
import sys

# date = sys.argv[1]
# word = sys.argv[2]
# date = cat(date.split('-'))
# gdeltFile = "s3://gdelt-open-data/events/"+date+"*" # read from S3
data = "s3://gdelt-open-data/events/2016"

spark = SparkSession.builder.appName("gdelt_analysis").getOrCreate()
gdeltData = spark.read.text(data).cache()

# count total No. of events on the given date
total =  data.count()

print data.first()
# linesWithWord = gdeltData.filter(gdeltData.value.contains(word))
# numLines = linesWithWord.count()

# print "total events = ", total_events
# print "first 10 lines with word", word, " in it ", linesWithWord.take(5)
# print "total number of lines with word",word," in it ", numLines
spark.stop()
