#!/usr/bin/python
# -*- coding: UTF-8 -*-

from MysqlUtils import mysql_client_connect
import redis


if __name__ == '__main__':
    conn = mysql_client_connect()
    if not conn:
        print 'failed to connect to mysql'
        return
    cur = conn.cursor()
    cache = redis.Redis(host='localhost', port=6379, db=0)
    keys = cache.keys()
    print 'json records: {num}'.format(num=len(keys))
    invalid_cnt = 0
    for date in keys:
        if len(cache[date]) < 10:
            invalid_cnt = invalid_cnt + 1
            continue
        sql = 'insert into dailylists(date, json_content) \
                values({date}, \'{json_content}\');' \
                .format(date=int(date), json_content=conn.escape_string(cache[date]))
        cur.execute(sql)
    cur.close()
    conn.commit()
    print 'failed to insert {num} records'.format(num=invalid_cnt)
    conn.close()
