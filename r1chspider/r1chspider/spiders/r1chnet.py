# -*- coding: utf-8 -*-
# https://github.com/viciousstar/BitcointalkSpider/blob/master/BitcointalkSpider/spiders/btspider.py
# http://doc.scrapy.org/en/latest/intro/tutorial.html

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
#from BitcointalkSpider.items import User, Post, Thread
from scrapy import log
from r1chspider.items import R1ChspiderItem

class R1chnetSpider(scrapy.Spider):
    name = "r1chnet"
    allowed_domains = ['old.r1ch.net']
    start_urls = ['http://old.r1ch.net/forum/index.php?board=2.0']

    denyboard = ['http://old.r1ch.net/forum/index\.php\?board=9\.\d+']

    rules =  (
        Rule(LinkExtractor(
            allow = ("http://old.r1ch.net/forum/.*")),
            #callback = "extractPost",
            follow = True
        )
    )

#    # WORKS!
#    # grab all span links and print them
#    def parse(self, response):
#        for sel in response.xpath('//span'):
#            title = sel.xpath('a/text()').extract()
#            link = sel.xpath('a/@href').extract()
#            print title, link

#    # WORKS!
#    # grab all span links and print them using items
#    def parse(self, response):
#        for sel in response.xpath('//span'):
#            item = R1ChspiderItem()
#            item['title'] = sel.xpath('a/text()').extract()
#            item['link'] = sel.xpath('a/@href').extract()
#            if item['title'] and item['link']:
#                yield item

    # WORKS!
    # grab all span links and print them using items
    def parse(self, response):
        for sel in response.xpath('//span'):
            item = R1ChspiderItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            if item['title'] and item['link']:
                yield item
