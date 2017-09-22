# BTC-sentiment-analysis

This script checks comments related to bitcoin from Reddit and applies ML to perform a sentiment analysis on BTC.

### 1. Continuously scrape revelant data from various sources

##### Tools that can be used:
* [Scrapy](www.scrapy.org)

##### Data structure for text:

| Text | Time | Long | Lat | Sentiment | Magnitude | Source | Tool | Verified |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| String | Unix? | Decimal | Decimal | Decimal | Decimal | Url | Int | Bool |


### 2. Sentiment analysis via Google Cloud

Perform analysis on MySQL database if verified == False

### 3. Display results on a webpage
