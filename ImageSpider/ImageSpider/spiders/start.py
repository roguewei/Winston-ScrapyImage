# scrapy 启动类
# 如果不写该启动函数，则只能在命令行通过命令scrapy crawl spidername启动蜘蛛
from scrapy import cmdline
# 方式一：注意execute的参数类型为一个列表
# cmdline.execute('scrapy crawl ImgSpider'.split())
# 方式二:注意execute的参数类型为一个列表
cmdline.execute(['scrapy', 'crawl', 'ImgSpider'])
