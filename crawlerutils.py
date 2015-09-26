#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
import time
import json
import redis


def fetch_url_content(url, port, timeout):
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) \
            AppleWebKit/537.11 (KHTML, like Gecko)Chrome/23.0.1271.10 Safari/537.11')

    content = None
    try:
        response = urllib2.urlopen(req)
        content = response.read()
    except urllib2.HTTPError, e:
        print e.code
        print e.read()
    return content


def decode_article(article_id):

    artcles = redis.Redis(host='localhost', port=6379, db=1)
    content = artcles[article_id]
    json_content = json.loads(content)
    article_id = json_content['stories'][9]['id']
    title = json_content['stories'][9]['title']
    print article_id, title
    url = gen_article_url(article_id)
    article = fetch_url_content(url=url, port=80, timeout=15)
    print url, article


def gen_list_url(date):
    prefix_url = 'http://news.at.zhihu.com/api/4/news/before/'
    url = ''.join([prefix_url, date])
    return url


def gen_article_url(article_id):
    if type(article_id) != str:
        article_id = str(article_id)
    prefix_url = 'http://news-at.zhihu.com/api/4/news/'
    return ''.join([prefix_url, article_id])


def gen_api_date(from_year, to_year):
    date_list = []

    days_of_month = [
            31, 29, 31, 30,
            31, 30, 31, 31,
            30, 31, 30, 31
    ]

    today = int(time.strftime('%Y%m%d'))
    for year in range(int(from_year), int(to_year) + 1):
        for month in range(0, 12):
            delimit = '0' if month < 9 else ''
            date = ''.join([str(year), delimit, str(month + 1)])
            for day in range(1, days_of_month[month] + 1):
                delimit = '0' if day < 10 else ''
                tmp = ''.join([date, delimit, str(day)])
                if int(tmp) > today + 1:
                    return date_list
                else:
                    date_list.append(tmp)


if __name__ == '__main__':
    dates = gen_api_date(from_year=2013, to_year=2015)
    print dates
