# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class EcollectPipeline(object):
    def process_item(self, item, spider):
        return item

class MongoPipeline(object):

    @classmethod
    def from_settings(cls, settings):
        return cls(
            settings.get('MONGO_URL', 'mongodb://localhost:27017/'),
            settings.get('MONGO_DATABASE', 'scraper'),
        )

    def __init__(self, mongo_url, mongo_database):
        client = pymongo.MongoClient(mongo_url)
        self.db = client[mongo_database]

    def process_item(self, item, spider):
        collection = self.db[spider.name]
        collection.save(dict(item))
        return item