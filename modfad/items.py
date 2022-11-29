# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ModfadItem(scrapy.Item):
    # define the fields for your item here like:
    LINK = scrapy.Field()
    NAME_OF_EVENT = scrapy.Field()
    DATE = scrapy.Field()
    
