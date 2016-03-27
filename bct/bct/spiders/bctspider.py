# -*- coding: utf-8 -*-
import scrapy


class BctspiderSpider(scrapy.Spider):
    name = "bctspider"
    allowed_domains = ["bitcointalk.org"]
    start_urls = (
        'http://www.bitcointalk.org/',
    )

    def parse(self, response):
        pass
