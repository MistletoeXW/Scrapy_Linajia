# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiascrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    CreatedAt = scrapy.Field()
    UpdatedAt = scrapy.Field()
    PageId = scrapy.Field()
    City = scrapy.Field()
    Area = scrapy.Field()
    SecArea = scrapy.Field()
    Title = scrapy.Field()
    CommunityName = scrapy.Field()
    HouseType = scrapy.Field()
    Square = scrapy.Field()
    Toward = scrapy.Field()
    Decoration = scrapy.Field()
    Lift = scrapy.Field()
    Flood = scrapy.Field()
    TotalPrice = scrapy.Field()
    UnitPrice = scrapy.Field()
    Image = scrapy.Field()
