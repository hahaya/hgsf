#! /usr/bin/env python
#! coding:utf-8

'''
Created on 2014/9/15

@author: hahaya
'''


from hgsf.db.redis_api import RedisApi

if __name__ == '__main__':
    db = RedisApi()
    db.connect();
    db.set("name", "hahaya")
    db.set("author", "hahaya")
    db.set("email", "hahayacoder@gmail.com")
    db.delete("author")

    print 'get key:', db.get("name")
    print 'db size:', db.dbsize()
