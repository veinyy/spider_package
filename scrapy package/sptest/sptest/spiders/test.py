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
cookies={'lang':'zh',
'_ha_ses.xs.d15e':'5d910d8e527a91bc2f1fa5f358bad32fa2d070c9',
'sip':'19-C9-2D-28-1F-57-C2-B2-D7-E9-EC-09-C3-52-93-8B-DD-80-3A-2E-CE-AA-89-6B',
'hwsso_uniportal':'1F3BEDBABD9FD230DF80A08FE2225ACD59B889761C134086298FBDBCC2BA13774FD3648381CCC7EC0D2B13CA769DAE02528ADEE9693DC27DF02468FC39A275DE9612043DA1950F5B82CF61354A6E95DCDE94565E7BD1BBD668372432891964C55D4C52437955E2FF94DCB97254D23BDBCB2F967B9F713574CE36CA219B1B423FB649F8B281D9DB1F0F4ED5E98EBEC461',
'suid':'43-6F-15-65-1B-EF-93-5C-61-AC-B5-7A-0C-0C-53-A0',
'TS_think_language':'zh-cn',
'authmethod':'authpwd',
'_ga':'GA1.2.2039450903.1441258932',
'hwssotinter3':'24770722257331',
'HWFORUM_SESSION':'s92j4ioiv1k1je306gkcdeue63',
'_ha_ref.xs.d15e':'%5B%22%22%2C%22%22%2C1442157501%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
'logFlag':'in',
'_ha_id.xs.d15e':'43-6F-15-65-1B-EF-93-5C-61-AC-B5-7A-0C-0C-53-A0.1442157514.0.1442157514..',
'sid':'72-C3-05-75-56-B7-5E-74-D8-31-F3-41-51-72-83-F8-98-8B-18-1F-64-65-24-A0-0C-8B-F7-C3-65-99-2A-F1-31-41-73-38-18-C3-D3-B0',
'ttc':'1442228178232',
'online_update':'1442157500',
'hwssotinter':'C9-65-9E-D0-53-E1-C2-15-07-19-17-51-BD-42-F5-6C',
's_fid':'22B5489B3FD06E56-07C599F372993F3A',
'uid':'43-6F-15-65-1B-EF-93-5C-61-AC-B5-7A-0C-0C-53-A0',
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
