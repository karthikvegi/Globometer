# Unravel the World
Study whats happening across the world in realtime

# Idea
1. What if you could know where earthquakes are happening in the whole world?
2. What if we could know which locations in the world need immediate aid and for what reason?
3. What if you could know all the places on the earth where a pandemic is breaking out?
4. What if you could understand the emotions and sentiments of people after an event happened, say a new law is passed

# Data Source
GDELT, backed by Google Jigsaw, is creating a platform to fundamentally reimagine how we study the human world in realtime at a planetary scale. In essence, GDELT monitors the news all over the world, translates it from 100 languages, processes it to identify all events, counts, quotes, people, organizations, locations, themes, emotions, relevant imagery, video, and embedded social media posts, placed it into global context, and makes it available for enabling open research on the planet itself. 

Data refreshed every 15 minutes.

# Relevant Technologies
1. Kafka 
2. ElasticSearch
3. Spark
4. Cassandra? Google Big Table?
5. Flask

# Architecture
S3 -> Kafka -> Spark/ElasticSearch -> Cassandra/Big Table -> Flask
