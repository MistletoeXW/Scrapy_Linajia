# -*- coding: utf-8 -*-
import scrapy


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['sh.lianjia.com']
    start_urls = ['http://sh.lianjia.com/']

    def parse(self, response):
        pass
