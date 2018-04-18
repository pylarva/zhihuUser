# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymongo


class UserPipeline(object):
    def __init__(self):
        self.f = None

    def process_item(self, item, spider):
        """
        :param item:  爬虫中yield回来的对象
        :param spider: 爬虫对象 obj
        :return:
        """
        self.f.write('{}\n'.format(json.dumps(dict(item), ensure_ascii=False)))

    @classmethod
    def from_crawler(cls, crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """
        print('执行pipeline的from_crawler，进行实例化对象')
        return cls()

    def open_spider(self, spider):
        """
        爬虫开始执行时，调用
        :param spider:
        :return:
        """
        print('打开爬虫...')
        self.f = open('User.txt', 'a+')

    def close_spider(self, spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        print('关闭爬虫...')
        self.f.close()


class MongoPipeline(object):
    collection_name = 'users'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # 去重
        self.db[self.collection_name].update({'url_token': item['url_token']}, dict(item), True)
        return item
