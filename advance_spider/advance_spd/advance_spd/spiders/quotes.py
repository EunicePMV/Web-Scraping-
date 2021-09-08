import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath("//*[@class='quote']")
        for quote in quotes:
            yield{
            'Text': quote.xpath(".//*[@class='text']/text()").get(),
            'Author': quote.xpath(".//*[@itemprop='author']/text()").get(),
            'Tags': quote.xpath(".//*[@class='tag']/text()").getall()
            }
        nxt_page = response.xpath("//*[@class='next']/a/@href").get()
        nxt_page_url = response.urljoin(nxt_page)
        yield scrapy.Request(nxt_page_url) 