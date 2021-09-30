import scrapy
from scrapy.http import Request
import os
import glob
import csv
import mysql.connector

def product_info(response, value):
    return response.xpath("//th[text()='"+value+"']/following-sibling::td/text()").get()

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
        title =  response.xpath("//h1/text()").get()
        rating = response.xpath("//p[contains(@class, 'star-rating')]/@class").get()
        upc = product_info(response, 'UPC')
        product_type = product_info(response, 'Product Type')

        yield {'Title': title,
               'Ratings': rating,
               'Upc': upc,
               'Product_Type': product_type}

    # from csv to database
    def close(self, reason):
        csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)
        
        mydb = mysql.connector.connect(host='localhost',
                                       user='root',
                                       passwd='foo',
                                       database='books_db')
        cursor = mydb.cursor()
        cursor.execute('''DROP TABLE IF EXISTS books_table''')
        cursor.execute('''CREATE TABLE books_table(
                       title TEXT,
                       ratings TEXT,
                       upc TEXT,
                       product_type TEXT)''')
        row_count = 0
        with open(csv_file, newline='') as f:
            csv_data = csv.reader(f)
            for row in csv_data:
                if row_count != 0:
                    cursor.execute('''INSERT INTO books_table VALUES(%s, %s, %s, %s)''',
                                   (row[0],
                                    row[1],
                                    row[2],
                                    row[3]))
                row_count += 1
        mydb.commit()