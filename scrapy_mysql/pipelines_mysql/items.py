# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SqlItem(scrapy.Item):
    title = scrapy.Field()
    rating = scrapy.Field()
    upc = scrapy.Field()
    product_type = scrapy.Field()