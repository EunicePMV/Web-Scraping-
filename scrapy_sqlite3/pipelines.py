# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class ScrapySqlite3Pipeline:
    def __init__(self):
        self.connect()
        self.create_table()

    def connect(self):
        self.db = sqlite3.connect('books_db')
        self.cursor = self.db.cursor()

    def create_table(self):
        self.cursor.execute('''DROP TABLE IF EXISTS books_table''')
        self.cursor.execute('''CREATE TABLE books_table(
                               Title TEXT, Ratings TEXT, Upc TEXT, Product_Type TEXT)''')

    def process_item(self, item, spider):
        self.save_table(item)
        return item

    def save_table(self, item):
        self.cursor.execute('''INSERT INTO books_table VALUES(?,?,?,?)''',
                            (item['title'],
                             item['rating'],
                             item['upc'],
                             item['product_type']))
        self.db.commit()