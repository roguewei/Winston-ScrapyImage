# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
# 本类用来存放图片链接
import scrapy


class ImagespiderItem(scrapy.Item):
    imgurl = scrapy.Field()
    pass
