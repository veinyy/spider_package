# -*- coding: utf-8 -*-
#File name :spyders/mokospider.py
#Author:Jhonny Zhang
#mail:veinyy@163.com
#create Time : 2014-11-29
#############################################################################

from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from meitu.items import MeituItem
import re
from scrapy.http import Request
from scrapy.selector import Selector


class MokoSpider(CrawlSpider):
    name = "dlmv"
    allowed_domains = ["win4000.com"]
    start_urls=["http://www.win4000.com/meinv47387_1.html"]
    rules = {
        Rule(SgmlLinkExtractor(allow=('/meinv\d{5}_\d{1}\.html')),  callback = 'parse_img', follow=True),
        Rule(SgmlLinkExtractor(allow=('/meinv\d{5}\.html')),  callback = 'parse_img', follow=True),
    }
    def parse_img(self, response):
        urlItem = MeituItem()
        sel = Selector(response)
        for divs in sel.xpath("//div[@class='pic-meinv']"):
            img_url=divs.xpath("a/img[@class='pic-large']/@src").extract()
            urlItem['image_urls'] = img_url
            yield urlItem


