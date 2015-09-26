#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2


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


def gen_api_url(date):
    prefix_url = 'http://news.at.zhihu.com/api/4/news/before/'
    url = ''.join([prefix_url, date])
    return url


def gen_api_date(from_year, to_year):
    date_list = []

    days_of_month = [
            31, 29, 31, 30,
            31, 30, 31, 31,
            30, 31, 30, 31
    ]

    for year in range(int(from_year), int(to_year) + 1):
        for month in range(0, 12):
            delimit = '0' if month < 9 else ''
            date = ''.join([str(year), delimit, str(month + 1)])
            for day in range(1, days_of_month[month] + 1):
                delimit = '0' if day < 10 else ''
                date_list.append(''.join([date, delimit, str(day)]))
    return date_list
