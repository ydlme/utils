#!/usr/bin/python
# -*- coding: UTF-8 -*-


import redis
import json
from ArticlesJsonChecker import get_jsonerror_articleids
from MysqlUtils import mysql_client_connect


if __name__ == '__main__':
    conn = mysql_client_connect()
    if not conn:
        print 'failed to connect to mysql'
        return
    cur = conn.cursor()
    cache = redis.Redis(host='localhost', port=6379, db=1)
    keys = get_jsonerror_articleids()
    print 'json encoding error records: {num}'.format(num=len(keys))
    invalid_cnt = 0
    for id in keys:
        if not cache.exists(str(id)):
            print 'cache not exists: ', id
            continue
        content = cache[id]
        json_content = json.loads(content)
        title = json_content['title']
        sql = 'insert into long_articles(article_id, title, json_content) \
                values({id}, \'{title}\', \'{json_content}\');' \
                .format(id=int(id), title=conn.escape_string(title),
                        json_content=conn.escape_string(content))
        cur.execute(sql)
    cur.close()
    conn.commit()
    print 'failed to insert {num} records'.format(num=invalid_cnt)
    conn.close()
