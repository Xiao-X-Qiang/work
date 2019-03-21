# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    cover_url = scrapy.Field()
    director = scrapy.Field()
    editor = scrapy.Field()
    actor = scrapy.Field()
    type = scrapy.Field()
    language = scrapy.Field()
    pub_date = scrapy.Field()
    long_time = scrapy.Field()
    pass
