# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiascrapyItem(scrapy.Item):
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
    Start = scrapy.Field()
    Visit = scrapy.Field()
    Publish = scrapy.Field()
    BuildingType = scrapy.Field()
    OwnerShip = scrapy.Field()
    DownPaymentBudget = scrapy.Field()
    HouseUse = scrapy.Field()
    CompletionDate = scrapy.Field()
    Floor = scrapy.Field()
    Visit7 = scrapy.Field()
    Visit30 = scrapy.Field()
    CarouselImages = scrapy.Field()