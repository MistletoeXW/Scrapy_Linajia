# -*- coding: utf-8 -*-
import scrapy
import time
import re
import requests
from bs4 import BeautifulSoup
from LianJiaScrapy.items import LianjiascrapyItem

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['sh.lianjia.com']
    baseURL = 'http://sh.liajia.com/ershoufang/'
    start_urls = []


    def parse(self, response):
        pass
