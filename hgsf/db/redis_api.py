#! /usr/bin/env python
#! coding:utf-8

import redis

class RedisApi:

    def __init__(self, timout = 0):
        self.hostname = ""
        self.port = 6379
        self.db = 0
        self.pool = None
        self.connection = None

    def connect(self, hostname='localhost', port = 6379, db = 0):
        self.hostname = hostname
        self.port = port
        self.db = db
        self.pool = redis.ConnectionPool(host = self.hostname, port = self.port, db = self.db)
        self.connection = redis.Redis(connection_pool = self.pool)

    def set(self, key, value):
        self.connection.set(key, value)

    def append(self, key, value):
        self.connection.append(key, value)

    def delete(self, key):
        return self.connection.delete(key)

    def get(self, key):
        return self.connection.get(key)

    def strlen(self, key):
        return self.connection.strlen(key)

    def ttl(self, key):
        return self.connection.ttl(key)

    def dbsize(self):
        return self.connection.dbsize()
