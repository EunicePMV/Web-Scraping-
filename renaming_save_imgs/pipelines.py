# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os

class RenamingSaveImgsPipeline:
    def process_item(self, item, spider):
        os.chdir('/home/EunicePMV/scrapy/renaming_save_imgs/renaming_save_imgs/renaming_save_imgs/spiders/imgs/')

        if item['images'][0]['path']:
            new_image_name = item['title'][0] + '.jpg'
            new_image_path = 'full/' + new_image_name

            os.rename(item['images'][0]['path'], new_image_path)