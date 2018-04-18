# !/usr/bin/env python
# -*- coding:utf-8 -*-

# import pprint
# from pymongo import MongoClient
#
# c = MongoClient('mongodb://172.16.1.141:27017')
#
# db = c['test']
# collection = db['test-collection']
#
# s_1 = {'author': 'pylarva01'}
# post_1 = db.posts.insert_one(s_1).inserted_id
#
# print(pprint.pprint(db.posts.find_one()))

import redis
r = redis.Redis(host='172.16.1.141', port='6379', password='myredis')
r.set('foo', 'Bar')
print(r.get('foo'))
