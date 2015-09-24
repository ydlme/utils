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


def get_daily_urls(from_year, to_year):
    url_list = []

    days_of_month = [
            31, 29, 31, 30,
            31, 30, 31, 31,
            30, 31, 30, 31
    ]

    prefix_url = 'http://news.at.zhihu.com/api/4/news/before/'

    for year in range(int(from_year), int(to_year) + 1):
        for month in range(0, 12):
            if month < 9:
                url = ''.join([prefix_url,str(year), '0', str(month+1)])
            else:
                url = ''.join([prefix_url,str(year), str(month+1)])
            for day in range(1, days_of_month[month] + 1):
                url_list.append(''.join([url, '0' if day < 10 else '', str(day)]))
    return url_list


def crawling_dailylists(urls):
    for url in urls:
        content = fetch_url_content(url, port=80, timeout=15)
        if content:
            print content


if __name__ == '__main__':
    print "知乎日报数据抓取"
    urls = get_daily_urls(2013, 2013)
    crawling_dailylists(urls)
