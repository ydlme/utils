#!/usr/bin/python
# -*- coding: utf-8 -*-


import redis
from crawlerutils import fetch_url_content
from crawlerutils import gen_api_url


def get_invalid_dates(host, port, db):
    date_list = []
    cache = redis.Redis(host=host, port=port, db=db)
    for date in cache.keys():
        content = cache[date]
        if len(content) < 10:
            date_list.append([date, content])

    return date_list

if __name__ == '__main__':
    invalidset = get_invalid_dates(host='localhost', port=6379, db=0)
    print 'invalidset: ', invalidset
    for item in invalidset:
        date = item[0]
        url = gen_api_url(date)
        content = fetch_url_content(url=url, port=80, timeout=15)
        print 'refetch content:{content}'.format(content=content)

