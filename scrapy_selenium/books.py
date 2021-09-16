import scrapy

from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from selenium import webdriver

class BooksSpider(Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
 
    def start_requests(self):
        self.driver = webdriver.Chrome('/home/EunicePMV/chromedriver')
        self.driver.get('http://books.toscrape.com')

        sel = Selector(text=self.driver.page_source)
        for book in sel.xpath("//h3/a/@href").getall():
            url = "http://books.toscape.com/" + book
            yield Request(url, callback=self.parse)

    def parse(self, response):
        pass