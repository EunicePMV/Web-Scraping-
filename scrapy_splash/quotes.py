# using splash to get to the next page to and get
# render back to the page itself
# what is the difference between scraping a page with and without splash


import scrapy
from scrapy_splash import SplashRequest

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/js/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, 
                                callback=self.parse,
                                endpoint='render.html')

    def parse(self, response):
        for quote in response.xpath("//*[@class='quote']"):
            yield{'author': quote.xpath(".//*[@class='author']/text()").get(),
                  'text': quote.xpath(".//*[@class='text']/text()").get()}


        # lua_source code 
        script = """function main(splash)
               assert(splash:go(splash.args.url ))
               splash:wait(0.3)
               button = splash:select("li[class=next] a")
               splash:set_viewport_full()
               splash:wait(0.1)
               button:mouse_click()
               splash:wait(1)
               return {url = splash:url(),
                       html = splash:html()}
            end"""

        yield SplashRequest(url=response.url,
                           callback=self.parse,
                           endpoint='execute',
                           args={'lua_source': script})