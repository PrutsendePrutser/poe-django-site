# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PoeDataRetrievalItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PoEAffixBlock(scrapy.Item):
    # Affix type
    affix_type = scrapy.Field()

    # Affix contentdata from the site
    affix_data = scrapy.Field()


class PoEAffixItem(scrapy.Item):
    # Affix block
    affix_name = scrapy.Field()
    # Affix tiers
    affix_tier = scrapy.Field()
    # Affix ilvl
    affix_ilvl = scrapy.Field()
    # Affix things
    affix_description = scrapy.Field()
    # Affix value
    affix_value = scrapy.Field()
