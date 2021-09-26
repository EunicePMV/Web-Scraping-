import scrapy
import os 
import csv
import glob
from openpyxl import Workbook


class CsvConvertSpider(scrapy.Spider):
    name = 'csv_convert'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        h1_tags = response.xpath("//h1/a/text()").get()
        tags = response.xpath("//*[@class='tag-item']/a/text()").getall()

        yield {'h1 tags': h1_tags, 'tags': tags}

    def close(self, reason):
        csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)

        wb = Workbook()
        ws = wb.active

        with open(csv_file, 'r') as f:
            for row in csv.reader(f):
                ws.append(row)

        wb.save(csv_file.replace('.csv','') + '.xlsx')


