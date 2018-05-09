#jsonify creates a json representation of the response
from flask import request
from flask import jsonify
from flask import render_template
from cassandra.cluster import Cluster
from collections import OrderedDict
import simplejson as json

# importing Cassandra modules from the driver we just installed
cluster = Cluster(['ec2-54-212-219-13.us-west-2.compute.amazonaws.com',
                    'ec2-52-41-205-89.us-west-2.compute.amazonaws.com',
                    'ec2-52-24-85-58.us-west-2.compute.amazonaws.com',
                    'ec2-54-148-6-162.us-west-2.compute.amazonaws.com'])
session = cluster.connect('gdelt')

from flask import Flask
app = Flask(__name__)

@app.route('/monitor')
def query():
    return render_template("world_monitor.html")

@app.route("/monitor",methods=['POST'])
def query_post():
    country = request.json["country"]
    date = request.json["date"]
    period = request.json["period"].lower()
    query = ""
    query += "SELECT * FROM monthly WHERE country = %s and date = %s"
    result = session.execute(query, parameters = [country,int(date)])[0]

    def create_dict(ordermap):
        n_dict = {}
        for event in ordermap:
           n_dict[str(event)] = {str(key): value for key, value in ordermap[event].items()}
        return n_dict

    clean_dict = create_dict(result[2])
    total_mentions = clean_dict["event_count"]['total']
    clean_dict.pop('event_count',None)
    jsonresponse = {"Events":clean_dict}
    return str(jsonresponse)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
