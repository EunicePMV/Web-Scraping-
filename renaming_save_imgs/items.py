# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RenamingSaveImgsItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()

    image_urls = scrapy.Field()
    images = scrapy.Field()