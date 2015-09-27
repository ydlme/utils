#!/usr/bin/python
# -*- coding:UTF-8 -*-

from celery import Celery
from crawlerutils import fetch_url_content
import redis


app = Celery(backend='amqp', broker='amqp://')


@app.task
def redis_fetch_dailylist(date):
    prefix_url = 'http://news.at.zhihu.com/api/4/news/before/'
    cache = redis.Redis(host='localhost', port=6379, db=0)
    url = ''.join([prefix_url, date])
    content = fetch_url_content(url=url, port=80, timeout=15)
    if content:
        cache.set(date, content)
        return True
    return False
