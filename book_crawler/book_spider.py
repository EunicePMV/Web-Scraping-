import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookSpider(CrawlSpider):
    name = 'book_spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']
    
    rules = (
        Rule(LinkExtractor(deny_domains='google.com'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        yield{'URL': response.url}
