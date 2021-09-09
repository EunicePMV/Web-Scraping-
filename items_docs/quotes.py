import scrapy
from scrapy.loader import ItemLoader
from items_doc.items import ItemsDocItem  

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        l = ItemLoader(item=ItemsDocItem(), response=response)
        # for quote in response.xpath("//*[@class='quote']"): 
        l.add_xpath('txt', "//*[@class='text']/text()")
        l.add_xpath('author', "//*[@class='author']/text()")
        l.add_xpath('tags', "//*[@class='tag']/text()")

        return l.load_item()