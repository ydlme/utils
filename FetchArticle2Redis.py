#!/usr/bin/python
# -*- coding:UTF-8 -*-

from celery import Celery
from crawlerutils import fetch_url_content
from crawlerutils import gen_article_url
import redis


app = Celery(backend='amqp', broker='amqp://')


@app.task
def redis_fetch_article(article_id):
    article_id = str(article_id)
    cache = redis.Redis(host='localhost', port=6379, db=1)
    url = gen_article_url(article_id)
    content = fetch_url_content(url=url, port=80, timeout=15)
    if content:
        cache.set(article_id, content)
        return True
    return False
