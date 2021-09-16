from scrapy import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

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

        while True:
            try:
                nxt_page = self.driver.find_element_by_xpath("//a[text()='next']")
                sleep(3)
                self.logger.info('Sleep for 3 seconds.')
                nxt_page.click()
                
                sel = Selector(text=self.driver.page_source)
                for book in sel.xpath("//h3/a/@href").getall():
                    url = "http://books.toscape.com/catalogue" + book
                    yield Request(url, callback=self.parse)
            except NoSuchElementException:
                self.logger.info('Reach the last page.')
                self.driver.quit()
                break

    def parse(self, response):
        pass