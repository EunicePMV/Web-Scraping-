import scrapy
from scrapy.http import FormRequest

class LoginQuotesSpider(scrapy.Spider):
    name = 'login_quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/login']

    def parse(self, response):
        csrf_token = response.xpath("//*[@name='csrf_token']/@value").get() 
        yield FormRequest('http://quotes.toscrape.com/login', 
                        formdata={'csrf_token': csrf_token,
                                  'username': 'selflove',
                                  'password': 'selflove'},
                                   callback=self.parse_after_login)

    def parse_after_login(self, response):
        if response.xpath("//a[text()='Logout']"):
            self.log("Login Successfully")

