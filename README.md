![GitHub Logo](/images/title.png)
A dashboard to monitor the socio-political events happening on the global stage and how they are affecting the stability of countries

# Data Source
GDELT, backed by Google Jigsaw, monitors the world’s broadcast, print, and web news in realtime at a planetary scale. The dataset is available daily from the year 1979.

# Purpose
We want to look at the important socio-political events that are affecting the stability of the countries over time.
The data to process is ~ 2 TB at an event and sub-event levels. 

# Data Pipeline
![GitHub Logo](/images/pipeline.png)

![GitHub Logo](/images/processing.png)

# Choice of Database
The simplest model for storing time series data is creating a wide row of data for each source and the row should grow as needed to accommodate the data. Cassandra’s data model is an excellent fit for handling data in sequence regardless of datatype or size. When writing data to Cassandra, data is sorted and written sequentially to disk. When retrieving data by row key and then by range, you get a fast and efficient access pattern due to minimal disk seeks – time series data is an excellent fit for this type of pattern. 





