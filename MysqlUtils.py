#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import sys


def mysql_client_connect():
    conn = None
    reload(sys)
    sys.setdefaultencoding('utf-8')
    try:
        conn = MySQLdb.connect(host='localhost', user='root', charset='utf8',
                               passwd='mysqlroot', db='zhihudaily'
                               )
    except MySQLdb.Error, e:
        print e.args
        try:
            conn.rollback()
        except MySQLdb.Error, e:
            print e.args
    finally:
        return conn
