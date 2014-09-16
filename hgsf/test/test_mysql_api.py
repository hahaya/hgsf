#! /usr/bin/env python
#! coding:utf-8

'''
Created on 2014/9/15

@author: hahaya
'''

from hgsf.db.mysql_api import mysql_api

if __name__ == '__main__':
    db = MysqlApi()
	db.connect(passwd = '121001')
    db.select_db("test")

