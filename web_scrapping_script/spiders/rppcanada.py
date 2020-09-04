import scrapy
import json
import pymongo
from scrapy.crawler import CrawlerProcess

# setup the client, database and collection
mongoHost = "mongodb://localhost:27017"
dbName = "backend_test"
colName = "rpp"

client = pymongo.MongoClient(mongoHost)
db = client[dbName]
collection = db[colName]
collection.drop()

# declare spider/crawler class
class RppcanadaSpider(scrapy.Spider):
    name = 'rppcanada'
    allowed_domains = ['www.rrpcanada.org']
    start_urls = ['https://api.rrpcanada.org/products']

    custom_settings = {
        # setting 2 seconds as scrapping/download delay
        # reduce the frequencies of queries which prevents being a burden to website's server
        "DOWNLOAD_DELAY" : 2,
    }

    def parse(self, response):
        # read json file from api website
        result = json.loads(response.body)
        allProducts = result["content"]["content"]


        # loop through list of products
        for i, product in enumerate(allProducts, start=1):
            productName = product["description"]
            productTotalAvailable = product["aggregateDemandSupply"]

            # store each Critical Product as a JSON document
            collection.insert({ 
                "_id" : i,
                "productName" : productName, 
                "totalAvailable" : productTotalAvailable 
            })

# enable crawler run from the script
process = CrawlerProcess()
process.crawl(RppcanadaSpider)
# the script will block here until the crawling is finished
process.start()