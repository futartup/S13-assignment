# -*- coding: utf-8 -*-
import scrapy
from ..items import ImageCrawlerItem
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


class UnsplashSpider(scrapy.Spider):
    name = 'unsplash'
    #allowed_domains = ['pexels.com']
    start_urls = ['https://www.istockphoto.com/in/photos/fork?mediatype=photography&phrase=fork&sort=mostpopular#close']

    def parse(self, response):
        print(response)
        item = ImageCrawlerItem()
        img_urls = []
        resp = response.css('img')
        for r in resp:
            if 'src' in r.attrib:
                if 'https' in r.attrib['src']:
                    img_urls.append(r.attrib['src'])
        item['image_urls'] = img_urls
        return item

