#!/usr/bin/python
# -*- coding: UTF-8 -*-

from MysqlUtils import mysql_client_connect
import redis
import json


if __name__ == '__main__':
    conn = mysql_client_connect()
    if not conn:
        return
    cur = conn.cursor()
    cache = redis.Redis(host='localhost', port=6379, db=1)
    keys = cache.keys()
    print 'json records: {num}'.format(num=len(keys))
    invalid_cnt = 0
    for id in keys:
        if len(cache[id]) < 10:
            invalid_cnt = invalid_cnt + 1
            continue
        content = cache[id]
        json_content = json.loads(content)
        title = json_content['title']
        sql = 'insert into articles(id, title, json_content) \
                values({id}, \'{title}\', \'{json_content}\');' \
                .format(id=int(id), title=conn.escape_string(title),
                        json_content=conn.escape_string(content))
        cur.execute(sql)
    cur.close()
    conn.commit()
    print 'failed to insert {num} records'.format(num=invalid_cnt)
    conn.close()
