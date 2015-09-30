#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import json
import sys


def get_jsonerror_articleids():
    error_id = []
    reload(sys)
    sys.setdefaultencoding('utf-8')
    try:
        conn = MySQLdb.connect(host='localhost', user='root', charset='utf8',
                               passwd='mysqlroot', db='zhihudaily'
                               )

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
    except MySQLdb.Error, e:
        print e.args
        try:
            conn.rollback()
        except MySQLdb.Error, e:
            print e.args
    finally:
        if conn:
            conn.close()
        return error_id


if __name__ == '__main__':

    error_articleids = get_jsonerror_articleids()
    print error_articleids
    print 'the number of error json encoding articles:', len(error_articleids)
