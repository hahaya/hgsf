#! /usr/bin/env python
#! coding:utf-8

import redis

class RedisApi:

    def __init__(self, timout = 0):
        self.hostname = ""
        self.port = 6379
        self.db = 0
        self.connection = None

    def connect(self, hostname, port = 6379, db = 0):
        self.hostname = hostname
        self.port = port
        self.db = db
        self.connection = redis.StrictRedis(hostname, port, db)

    def set(self, key, value):
        self.connection.set(key, value)

    def get(self, key):
        return self.connection.get(key)
