#!/usr/bin/python
# -*- coding: UTF-8 -*-


from fetcharticle2redis import redis_fetch_article
import json
import redis

if __name__ == '__main__':
    dailylist = redis.Redis(host='localhost', port=6379, db=0)
    article_cnt, failed_cnt = 0, 0
    print 'begin fetch all articles'
    for date in dailylist.keys():
        content = dailylist[date]
        json_content = json.loads(content)
        try:
            stories = json_content['stories']
            for idx in range(0, len(stories)):
                article_id = stories[idx]['id']
                title = stories[idx]['title']
                print article_id, title
                article_cnt = article_cnt + 1
                redis_fetch_article.delay(article_id)
        except KeyError, e:
            print e
            failed_cnt = failed_cnt + 1
    print 'fetch article:', article_cnt
    print 'fetch failed:', failed_cnt
