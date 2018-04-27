# Monitor the World
Monitor the stability of countries across world and the important events that contribute to it

# Data Source
GDELT, backed by Google Jigsaw, is creating a platform to fundamentally reimagine how we study the human world in realtime at a planetary scale. In essence, GDELT monitors the news all over the world, translates it from 100 languages, processes it to identify all events, attaches a CAMEO (Conflict and Mediation Observation) code and given a Goldstein score (-10 to +10) capturing the potential impact of the event.

# What is the data and engineering problem?
We are implementing an algorithm to compute the stability of the country based on the events and their impact. 

The data to process is TB scale and it is an at event and sub-event levels.The events and sub-events need to be identified, joined to the event-mentions, and use different features like num-mentions, num-sources, no-articles, geo-type (city/state/country), avg-doc-tone by looking at all the mentions of the news/articles of the event and aggregate is to various levels of granularity to observe the stability of a country over a period of time.
 
# Relevant Technologies
1. S3
2. Spark/Spark SQL
3. MySQL
4. Flask
5. ElasticSearch

# Data Pipeline
![GitHub Logo](/images/data-pipeline.png)

