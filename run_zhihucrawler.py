#!/usr/bin/python
# -*- coding: UTF-8 -*-


from crawlerutils import gen_api_date
from store2redis import redis_insert


if __name__ == '__main__':
    dates = gen_api_date(2013, 2015)
    for date in dates:
        redis_insert.delay(date)
