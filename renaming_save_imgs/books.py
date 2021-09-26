import scrapy
from scrapy.http import Request
from scrapy.loader import ItemLoader
from renaming_save_imgs.items import RenamingSaveImgsItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        books_url = response.xpath("//h3/a/@href").getall()
        for book in books_url:
            absolute_url_book = response.urljoin(book)
            yield Request(absolute_url_book, callback=self.parse_book)

    def parse_book(self, response):
        l = ItemLoader(item=RenamingSaveImgsItem(), response=response)

        title =  response.xpath("//h1/text()").get()
        price = response.xpath("//p[@class='price_color']/text()").get()

        image_urls = response.xpath("//img/@src").get()
        image_urls = image_urls.replace("../..", self.start_urls[0])

        l.add_value('title', title)
        l.add_value('price', price)
        l.add_value('image_urls', image_urls)

        return l.load_item() 
