# 开发Scrapy爬虫的步骤

创建项目：scrapy startproject xxx（项目名字，不区分大小写）
明确目标 （编写items.py）：明确你想要抓取的目标
制作爬虫 （spiders/xxspider.py）：制作爬虫开始爬取网页
存储内容 （pipelines.py）：设计管道存储爬取内容
启动程序的py文件（start.py）：等同于此命令（scrapy crawl xxx -o xxx.json）
from scrapy import cmdline
cmdline.execute("scrapy crawl 项目名".split())


# 爬虫中的常用命令
stratproject 创建一个新工程 scrapy startproject<name> [dir]
genspider 创建一个爬虫 scrapy genspider [options] <name> <domain>
例如 scrapy genspider baidu baidu.com
settings 获取爬虫配置信息 scrapy settings [options]
crawl 运行一个爬虫 scrapy crawl <spider>
list 列出工程中所有爬虫 scrapy list
shell 启动URL调试命令行 scrapy shell [url]


# scrapy保存信息的最简单的方法主要有七种格式
json格式，默认为Unicode编码
scrapy crawl 项目名 -o 项目名.json
json lines格式，默认为Unicode编码
scrapy crawl 项目名 -o 项目名.jsonlines
csv 逗号表达式，可用Excel打开
scrapy crawl 项目名 -o 项目名.csv
xml格式
scrapy crawl 项目名 -o 项目名.xml


# Parse()方法的工作机制
1. 因为使用的yield，而不是return。parse函数将会被当做一个生成器使用。scrapy会逐一获取parse方法中生成的结果，并判断该结果是一个什么样的类型；
2. 如果是request则加入爬取队列，如果是item类型则使用pipeline处理，其他类型则返回错误信息。
3. scrapy取到第一部分的request不会立马就去发送这个request，只是把这个request放到队列里，然后接着从生成器里获取；
4. 取尽第一部分的request，然后再获取第二部分的item，取到item了，就会放到对应的pipeline里处理；
5. parse()方法作为回调函数(callback)赋值给了Request，指定parse()方法来处理这些请求 scrapy.Request(url, callback=self.parse)
6. Request对象经过调度，执行生成 scrapy.http.response()的响应对象，并送回给parse()方法，直到调度器中没有Request（递归的思路）
7. 取尽之后，parse()工作结束，引擎再根据队列和pipelines中的内容去执行相应的操作；
8. 程序在取得各个页面的items前，会先处理完之前所有的request队列里的请求，然后再提取items。
7. 这一切的一切，Scrapy引擎和调度器将负责到底。


