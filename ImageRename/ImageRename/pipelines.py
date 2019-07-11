# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class ImagerenamePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        print("get_media_requests=============")
        # 循环每一张图片地址下载
        for image_url in item['imgurl']:
            # meta里面的数据是从spider获取，然后通过meta传递给下面的方法：file_path
            yield Request(image_url, meta={'name': item['imgname']})

    # 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
    def file_path(self, request, response=None, info=None):
        print("file_path--------------")
        # 提取URL前面的名称作为图片名
        image_guid = request.url.split('/')[-1]
        # 接收上面meta传递过来的图片名称
        name = request.meta['name']
        # 过滤Windows字符串，不经过这个步骤，会有乱码或者无法下载
        name = re.sub(r'[？\\*|“<>:/]', '', name)
        # 分文件夹存储的关键：{0}对应着name；{1}对应着image_guid
        filename = u'{0}/{1}'.format(name, image_guid)
        return filename
