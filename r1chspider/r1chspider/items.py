# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class R1ChspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    title = scrapy.Field()
    link = scrapy.Field()


# store user's infromation
class User(scrapy.Item):
    name = scrapy.Field()
    posts = scrapy.Field()
    activity = scrapy.Field()
    position = scrapy.Field()
    registerDate = scrapy.Field()
    lastDate = scrapy.Field()
    Email = scrapy.Field()
    gender = scrapy.Field()
    age = scrapy.Field()
    bitcoinAddress = scrapy.Field()
    year = scrapy.Field()
    month = scrapy.Field()
    day = scrapy.Field()

# store posts' information
class Thread(scrapy.Item):
    topic = scrapy.Field()
    time = scrapy.Field()
    # include every post'(include re) all content(topic, author, time, content)
    content = scrapy.Field()
    url = scrapy.Field()
    ofBoard = scrapy.Field()
    user = scrapy.Field()
    year = scrapy.Field()
    month = scrapy.Field()
    day = scrapy.Field()
    flag = scrapy.Field()  #Thread if 1 else 0
