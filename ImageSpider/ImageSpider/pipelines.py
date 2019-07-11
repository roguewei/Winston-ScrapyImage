# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 本类是图片下载中间件
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class ImagespiderPipeline(ImagesPipeline):
    # 这个方法主要是把蜘蛛yield过来的图片链接执行下载
    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in item['imgurl']:
            # print(image_url+"------------------")
            yield Request(image_url)

    # 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
    def file_path(self, request, response=None, info=None):
        print(request.url)
        image_guid = request.url.split('/')[-1]  # 提取url前面名称作为图片名。
        return image_guid
