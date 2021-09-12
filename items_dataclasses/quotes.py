import scrapy
from scrapy.loader import ItemLoader
from quotes_dataclasses.items import QuotesDataclassesItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        l = ItemLoader(QuotesDataclassesItem(), response=response)
        l.add_xpath('txt', "//*[@class='text']/text()")
        l.add_xpath('author', "//*[@class='author']/text()")
        l.add_xpath('tags', "//*[@class='tag']/text()")

        return l.load_item()
