# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanMovieItems(scrapy.Item):
    ranking=scrapy.Field()
    movie_name=scrapy.Field()
    score=scrapy.Field()
    score_num=scrapy.Field()