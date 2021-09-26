import scrapy
from scrapy_items_example.items import ScrapyItemsExampleItem

 # get the author, and modify the items.py


class SampleItemsSpiderSpider(scrapy.Spider):
    name = 'sample_items_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        authors = response.xpath("//*[@class='author']/text()").getall()
        
        items = ScrapyItemsExampleItem()
        items['authors'] = authors

        return items