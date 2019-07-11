# -*- coding: utf-8 -*-
# 该文件是scrapy genspider baidu baidu.com命令生成的
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
