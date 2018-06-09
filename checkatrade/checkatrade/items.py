# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CheckatradeItem(scrapy.Item):
    contact_name = scrapy.Field()
    company_name = scrapy.Field()
    address = scrapy.Field()
    phone_number = scrapy.Field()
    email = scrapy.Field()