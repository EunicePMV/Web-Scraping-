# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from scrapy.utils.project import get_project_settings

class ScrapyMongodbPipeline(object):
    def __init__(self):
        # import settings
        settings = get_project_settings()

        # establish the connection in mongodb
        client = MongoClient(settings['MONGODB_SERVER'],
                             settings['MONGODB_PORT'])

        # get and create the db
        db = client[settings['MONGODB_DB']]

        # get the collection name and create 
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        # insert all scraped items into the mongodb database
        self.collection.insert(dict(item))
        return item
