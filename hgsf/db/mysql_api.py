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
        self.connection = None

    def connect(self, 
                hostname = "localhost", 
                port = 3306, 
                user = "root", 
                passwd = "", 
                db = ""):
        self.hostname = hostname
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.connect = MySQLdb.connect(host = self.hostname, port = self.port, user = self.user, passwd = self.passwd, db = self.db)
