import scrapy
from scrapy.http import Request

def product_info(response, value):
    return response.xpath("//th[text()='"+value+"']/following-sibling::td/text()").get()


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        books_url = response.xpath("//h3/a/@href").getall()
        for book in books_url:
            absolute_url_book = response.urljoin(book)
            yield Request(absolute_url_book, callback=self.parse_book)

        nxt_page = response.xpath("//li[@class='next']/a/@href").get()
        nxt_page_url = response.urljoin(nxt_page)
        yield Request(nxt_page_url)


    def parse_book(self, response):
        title =  response.xpath("//h1/text()").get()
        price = response.xpath("//p[@class='price_color']/text()").get()
        
        img_url = response.xpath("//img/@src").get()
        img_url = img_url.replace("../..", self.start_urls[0])

        star_rating = response.xpath("//p[contains(@class, 'star-rating')]").get()
        rating = ''
        for i in range(10, 26+1):
            rating += star_rating[i]

        description = response.xpath("//div[@id='product_description']/following-sibling::p/text()").get()

        upc = product_info(response, 'UPC')
        product_type = product_info(response, 'Product Type')
        price_no_tax = product_info(response, 'Price (excl. tax)')
        price_with_tax = product_info(response, 'Price (incl. tax)')
        tax = product_info(response, 'Tax')
        availability = product_info(response, 'Availability')
        no_of_reviews = product_info(response, 'Number of reviews')

        yield {'Title': title,
               'Price': price,
               'Image Source': img_url,
               'Ratings': rating,
               'Description': description,
               'UPC': upc,
               'Product Type': product_type,
               'Price with tax': price_with_tax,
               'Price with no tax': price_no_tax,
               'Tax': tax,
               'Availability': availability,
               'Number of reviews': no_of_reviews
               }








