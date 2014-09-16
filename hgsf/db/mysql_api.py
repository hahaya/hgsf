#! /usr/bin/env python
#! coding:utf-8

'''
Created on 2014/9/15

@author: hahaya
'''

import MySQLdb

class MysqlApi:

    def __init__(self):
        self.hostname = "localhost"
        self.port = 3306
        self.user = "root"
        self.passwd = ""
        self.db = ""
        self.charset = "utf8"
        self.connection = None
        self.cursor = None

    def connect(self,
                hostname = "localhost",
                port = 3306,
                user = "root",
                passwd = "",
                db = "",
                charset = "utf8"):
        self.hostname = hostname
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset
        self.connection = MySQLdb.connect(host = self.hostname, port = self.port, user = self.user, passwd = self.passwd, db = self.db)
        self.connection.set_character_set(self.charset)
        self.cursor = self.connection.cursor()

    def select_db(self, db):
        try:
            self.connection.select_db(db)
        except MySQLdb.Error as e:
            print("Mysql Error %d:%s" % e.args[0], e.args[1])

    def query(self, sql):
        try:
            return self.cursor.execute(sql)
        except MySQLdb.Error as e:
            print("Mysql Error:%s\n SQL:%s" % (e, sql))
