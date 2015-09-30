#!/usr/bin/python
# -*- coding: UTF-8 -*-


from fetcharticle2redis import redis_fetch_article
from ArticlesJsonChecker import get_jsonerror_articleids


if __name__ == '__main__':
    article_cnt, failed_cnt = 0, 0
    print 'begin fetch long articles'
    error_ids = get_jsonerror_articleids()
    print 'begin crawling {total} long articles'.format(total=len(error_ids))
    for article_id in error_ids:
        redis_fetch_article.delay(article_id)
