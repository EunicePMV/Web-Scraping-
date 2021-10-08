import scrapy
from scrapy.http import FormRequest
import logging

class HkexnewsSpider(scrapy.Spider):
    name = 'hkexnews'
    allowed_domains = ['hkexnews.hk']
    start_urls = ['https://www.hkexnews.hk/sdw/search/searchsdw.aspx']

    def parse(self, response):
        data = {'__EVENTTARGET': 'btnSearch',
        '__VIEWSTATE': response.xpath("//*[@name='__VIEWSTATE']/@value").get(),
        '__VIEWSTATEGENERATOR': response.xpath("//*[@name='__VIEWSTATEGENERATOR']/@value").get(),
        'today': '20211008',
        'sortBy': 'shareholding',
        'sortDirection': 'desc',
        'txtShareholdingDate': '2021/10/07',
        'txtStockCode': '00001',
        'txtStockName': 'CK HUTCHISON LIMITED'}

        return FormRequest(self.start_urls[0],
                           formdata=data,
                           callback=self.after_post)

    def after_post(self, response):
        logging.info(response)