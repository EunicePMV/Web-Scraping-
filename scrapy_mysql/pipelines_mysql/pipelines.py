# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class SqlPipeline:
    def __init__(self):
        self.connect()
        self.save_table()

    def connect(self):
        self.db = mysql.connector.connect(host='localhost',
                                          user='root',
                                          passwd='foo',
                                          database='books_db')
        self.cursor = self.db.cursor()

    def save_table(self):
        self.cursor.execute('''DROP TABLE IF EXISTS books_table''')
        self.cursor.execute('''CREATE TABLE books_table(
                            title TEXT,
                            rating TEXT,
                            upc TEXT,
                            product_type TEXT)''')

    def process_item(self, item, spider):
        self.save_item(item)
        return item

    def save_item(self, item):
        self.cursor.execute('''INSERT INTO books_table VALUES(%s, %s, %s, %s)''',
                            (item['title'],
                            item['rating'],
                            item['upc'],
                            item['product_type']))
        self.db.commit()
