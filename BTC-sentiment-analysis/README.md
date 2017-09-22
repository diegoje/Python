# BTC-sentiment-analysis

This script checks comments related to bitcoin from multiple sources and applies ML to perform a sentiment analysis on BTC.

### 1. Continuously scrape revelant data from various sources

##### Tools that can be used for scraping/analysis:
* [Scrapy](www.scrapy.org)

##### Structure for saving data (MySQL database):

| Text | Time | Long | Lat | Sentiment | Magnitude | Source | Tool | Verified |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| String | Unix? | Decimal | Decimal | Decimal | Decimal | Url | Int | Bool |


### 2. Sentiment analysis via Google Cloud

Continuously perform analysis on MySQL database `if verified == False`

### 3. Display results on a webpage

* Charts using [this tool](www.highcharts.com)
* Interactive 3D globe using [this tool](https://experiments.withgoogle.com/chrome/globe)