#!/usr/bin/python
# -*- coding: UTF-8 -*-

from MysqlUtils import mysql_client_connect
import json


def get_jsonerror_articleids():
    error_id = []
    conn = mysql_client_connect()
    if not conn:
        return []
    cur = conn.cursor()
    sql = 'select max(id) from articles'
    cur.execute(sql)
    max_id = int(cur.fetchone()[0])
    min_id, row_size = 0, 3000
    for sep in range(0, max_id + 1, row_size):
        ender = min_id + row_size
        ender = ender if ender < max_id else max_id
        sql = 'select article_id, json_content from articles where id > {min_id}\
            and id < {ender};'.format(min_id=min_id, ender=ender)
        cur.execute(sql)
        rows = cur.fetchall()
        for row in rows:
            try:
                json.loads(str(row[1]))
            except ValueError, e:
                error_id.append(row[0])
    conn.close()
    return error_id


if __name__ == '__main__':

    error_articleids = get_jsonerror_articleids()
    print error_articleids
    print 'the number of error json encoding articles:', len(error_articleids)
