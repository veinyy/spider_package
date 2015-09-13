from scrapy.spider import Spider
from scrapy.http import Request, FormRequest
from scrapy.linkextractors import LinkExtractor
from sptest.items import SptestItem
import scrapy
import time

class MySpider(Spider):
    name = 'myspider'
    allowed_domains = ['huawei.com']
    start_urls = [
        'http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=467&cate=58&p=1',
        'http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=409&cate=44&p=',
        'http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=466&cate=52&p=',
        'http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=468&cate=64&p=',
        'http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=899&cate=149&p=',
        'http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=469&cate=70&p=',
        'http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=470&cate=76&p=',
        'http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=507&cate=88&p=',
        'http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=508&cate=94&p=',
        'http://xinsheng.huawei.com/cn/index.php?app=forum&mod=List&act=index&class=509&cate=100&p=',
        ]
   # rules = (Rule(LinkExtractor(restrict_xpaths=('//div[@class="bbs_page fr"]/form/ul/a[2]/@href')), callback = 'parse_item',follow=True),)

    def start_requests(self):
        yield Request(url=self.start_urls[0],callback=self.parse_otherurl,
cookies={
})
    def parse_otherurl(self,response):
        for i in range(len(self.start_urls)):
            for val in range(100):
                target_url = self.start_urls[i] + str(val)
                yield Request(url=target_url, callback=self.parse_item)


    def parse_item(self, response):
        items=SptestItem()
        for desc in  response.xpath("//div[@class='title']/p"):
            items["link"] = desc.xpath("a/@href").extract()
            items["name"] = desc.xpath("a/@title").extract()
            yield items
