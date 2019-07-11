import scrapy
from ImageRename.items import ImagerenameItem


class ImgsrenameSpider(scrapy.Spider):
    name = 'ImgsRename'
    allowed_domains = [
        'lab.scrapyd.cn'
    ]
    start_urls = [
        'http://lab.scrapyd.cn/archives/55.html',
        'http://lab.scrapyd.cn/archives/57.html',
    ]

    def parse(self, response):
        # 实例化item
        item = ImagerenameItem()
        item['imgurl'] = response.css('.post img::attr(src)').extract()
        # 抓取文章标题作为图集名称
        item['imgname'] = response.css('.post-title a::text').extract_first()
        yield item
