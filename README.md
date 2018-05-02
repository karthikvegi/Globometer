# Monitor the World
Monitor the stability of countries across world and the important events that contribute to it

# Data Source
GDELT, backed by Google Jigsaw, is creating a platform to fundamentally reimagine how we study the human world in realtime at a planetary scale. In essence, GDELT monitors the news all over the world, translates it from 100 languages, processes it to identify all events happening around the world.

# What is the use case?
We are implementing an algorithm to compute the stability of the country based on the events and their impact. 

The data to process is ~ 1 TB and it is an at event and sub-event levels.The events and sub-events need to be identified, joined to the event-mentions, and use different features like num-mentions, num-sources, no-articles, geo-type (city/state/country), avg-doc-tone by looking at all the mentions of the news/articles of the event and aggregate is to various levels of granularity to observe the stability of a country over a period of time.

# Data Pipeline
![GitHub Logo](/images/pipeline.png)

# Choice of Database
The simplest model for storing time series data is creating a wide row of data for each source and the row should grow as needed to accommodate the data. Cassandra’s data model is an excellent fit for handling data in sequence regardless of datatype or size. When writing data to Cassandra, data is sorted and written sequentially to disk. When retrieving data by row key and then by range, you get a fast and efficient access pattern due to minimal disk seeks – time series data is an excellent fit for this type of pattern. 





