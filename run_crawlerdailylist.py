#!/usr/bin/python
# -*- coding: UTF-8 -*-


from crawlerutils import gen_api_date
from fetchdailylist2redis import redis_fetch_dailylist


if __name__ == '__main__':
    dates = gen_api_date(2013, 2015)
    for date in dates:
        redis_fetch_dailylist.delay(date)
