#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import redis

if __name__ == '__main__':
    try:
        conn = MySQLdb.connect(host='localhost', user='root', passwd='mysqlroot', db='zhihudaily')
        cur = conn.cursor()
        cache = redis.Redis(host='localhost', port=6379, db=0)
        for date in cache.keys():
            print '持续化数据:', date
            sql = 'insert into dailylists(date, json) \
                    values({date}, \'{json}\');'.format(date=int(date), json=cache[date])
            cur.execute(sql)
        cur.close()
        conn.commit()
    except MySQLdb.Error, e:
        print e.args
        try:
            conn.rollback()
        except MySQLdb.Error, e:
            print e.args
    finally:
        if conn:
            conn.close()
