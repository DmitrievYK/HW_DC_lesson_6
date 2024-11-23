# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, Compose

def annotation_clear(values):
    if isinstance(values, list):# Обработка если входное значение это список
        values = ' '.join(values)  # Объединяем значения списка в одну строку
    return values.replace("\n", " ").strip()

class UnsplashparserItem(scrapy.Item):

    name = scrapy.Field(output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    tags = scrapy.Field()
    annotation_img = scrapy.Field(input_processor=Compose(annotation_clear), output_processor=TakeFirst())
    img_url = scrapy.Field(output_processor=TakeFirst())
    
