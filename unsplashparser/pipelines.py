# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
### pip install pillow
import csv
import scrapy 
from typing import Any
from scrapy.pipelines.images import ImagesPipeline



class UnsplashparserPipeline:
    def __init__(self):
        self.csv_file = open('unsplash_data.csv', 'w', newline='', encoding="utf-8")
        self.csv_write = csv.writer(self.csv_file)
        self.csv_write.writerow(["name", "url", "tags", "annotation_img", "img_url"])
    
    def close_spider(self, spider):
        self.csv_file.close()

    def process_item(self, item, spider):
        self.csv_write.writerow([
            item.get('name'),
            item.get('url'),
            item.get('tags'),
            item.get('annotation_img'),
            item.get('img_url')
        ])
        return item

class UnsplashImg(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['img_url']:
            try:
                yield scrapy.Request(item['img_url'])
            except Exception as e:
                print(e)

    
    def item_completed(self, results, item, info):
        if results:
            item['img_url'] = [itm[1] for itm in results]
                
        return item
