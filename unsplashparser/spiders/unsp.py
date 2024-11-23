from typing import Any
import scrapy
from scrapy.http import HtmlResponse
from unsplashparser.items import UnsplashparserItem
from scrapy.loader import ItemLoader


class UnspSpider(scrapy.Spider):
    name = "unsp"
    allowed_domains = ["unsplash.com"]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f"https://unsplash.com/s/photos/{kwargs.get('query')}"]

    def parse(self, response:HtmlResponse):

        links = response.xpath("//div[@class='_cnA1']//a[@itemprop='contentUrl']")
        for link in links:
            yield response.follow(link, callback=self.parse_pht)
            
        
    def parse_pht(self, response:HtmlResponse):
       
        loader = ItemLoader(item=UnsplashparserItem(), response=response)
        loader.add_xpath("name", "//h1/text()")
        loader.add_value("url", response.url)
        loader.add_xpath("tags", "//div[@class='zb0Hu atI7H']/a/text()")
        loader.add_xpath("annotation_img", "//div[@class='CjEYU jhw7y']/p/text()")
        loader.add_xpath("img_url", "//button[@class='HrSOP QcIGU x8A7E LAl8f']//img[2]/@src")

        yield loader.load_item()

        # name = response.xpath("//h1/text()").get()
        # url = response.url
        # tags = response.xpath("//div[@class='zb0Hu atI7H']/a/text()").getall()
        # # tags_url = response.xpath("//div[@class='zb0Hu atI7H']/a/@href").getall()
        # annotation_img = response.xpath("//div[@class='CjEYU jhw7y']/p/text()").getall()
        # img_url = response.xpath("//button[@class='HrSOP QcIGU x8A7E LAl8f']//img[2]/@src").getall()

        # yield UnsplashparserItem(name=name, url=url, tags=tags, annotation_img=annotation_img, img_url=img_url)
