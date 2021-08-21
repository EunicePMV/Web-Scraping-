import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
        ]

    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            yield{
                'author': quote.css('.author::text').get(),
                'text' : quote.css('.text::text').get(),
                'tags' : quote.css('.tag::text').getall()
            }
        nxt_page = response.css('.next a::attr(href)').get()
        if int(nxt_page[-2]) <= 5:
            nxt_page = response.urljoin(nxt_page)
            yield scrapy.Request(nxt_page, callback=self.parse)