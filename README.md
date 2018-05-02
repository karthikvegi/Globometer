# Globometer
A dashboard to monitor the socio-political events happening on the global stage and how they are affecting the stability of countries over time

# Data Source
GDELT, backed by Google Jigsaw, monitors the world’s broadcast, print, and web news in realtime at a planetary scale. The dataset is available daily from the year 1979.

# What is the use case?
We are computing the stability of the country based on the events and their impact. 
The data to process is ~ 0.5TB at an event and sub-event levels.The events and sub-events need to be identified, joined to the event-mentions, and using features like num-mentions, num-sources, num-articles, geo-type (city/state/country), avg-doc-tone by looking at all the mentions of the news/articles of the event and aggregate it to various levels of granularity to observe the socio-political stability of a country over a period of time.

# Data Pipeline
![GitHub Logo](/images/pipeline.png)

# Choice of Database
The simplest model for storing time series data is creating a wide row of data for each source and the row should grow as needed to accommodate the data. Cassandra’s data model is an excellent fit for handling data in sequence regardless of datatype or size. When writing data to Cassandra, data is sorted and written sequentially to disk. When retrieving data by row key and then by range, you get a fast and efficient access pattern due to minimal disk seeks – time series data is an excellent fit for this type of pattern. 





