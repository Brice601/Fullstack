import scrapy
import os
import logging
from scrapy.crawler import CrawlerProcess

class imdb_spider(scrapy.Spider):
    # nom de la spider
    name = "imdb"

    # url au départ pour la spider
    start_urls = [
        "https://www.imdb.com/chart/boxoffice",
    ]

    # Callback function that will be called when starting your spider
    # This spider should scrape the ranking, the title, the url, the total earnings, the rating and the number of voters for the first movie of the charts
    def parse(self, response):
        # title h3 : 
        # /html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div/div/div/div/div[2]/div/a/h3      
        # /html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[2]/div/div/div/div/div[2]/div/a/h3       
        # /html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[3]/div/div/div/div/div[2]/div/a/h3

        #total earnings : 
        # /html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div/div/div/div/div[2]/ul/li[2]/span[2]
        # /html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[2]/div/div/div/div/div[2]/ul/li[2]/span[2]

        #rating and 
        # /html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div/div/div/div/div[2]/span/div/span/span[1]
        # /html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[2]/div/div/div/div/div[2]/span/div/span/span[1]
        # 
        # number of voters
        # /html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div/div/div/div/div[2]/span/div/span/span[2]
        # /html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[2]/div/div/div/div/div[2]/span/div/span/span[2]

        imdb = response.xpath("/html/body/div[2]/main/div/div[3]/section/div/div[2]/div/ul/li[1]/div/div/div/div/div[2]")
        return{
            "title": imdb.xpath("/div/a/h3/text()").get(),
            "total_earnings": imdb.xpath("ul/li[2]/span[2]/text()").get(),
            "rating": imdb.xpath("span/div/span/span[1]/text()").get(),
            "voters": imdb.xpath("span/div/span/span[2]/text()").get()
        }

# Name of the file where the results will be saved
filename = "imdb1.json"

# If file already exists, delete it before crawling (because Scrapy will 
# concatenate the last and new results otherwise)
if filename in os.listdir("src/"):
    os.remove("src/" + filename)

# Declare a new CrawlerProcess with some settings
## USER_AGENT => Simulates a browser on an OS
## LOG_LEVEL => Minimal Level of Log 
## FEEDS => Where the file will be stored 
## More info on built-in settings => https://docs.scrapy.org/en/latest/topics/settings.html?highlight=settings#settings
process = CrawlerProcess(settings = {
    "USER_AGENT": "Firefox/141.0",
    "LOG_LEVEL": logging.INFO,
    "FEED": {
        "src/" + filename : {"format": "json"},
    }
})

# Start the crawling using the spider you defined above
process.crawl(imdb_spider)
process.start()