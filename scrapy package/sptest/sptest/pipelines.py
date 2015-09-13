# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import time

class SptestPipeline(object):
    def __init__(self):
        self.file = codecs.open('info_marry.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        line1 = json.dumps(dict(item), ensure_ascii=False) + "\n"
        gn="姑娘".decode('utf-8')
        mz="妹子".decode('utf-8')
        nv="女".decode('utf-8')
        if (gn in line1) or (mz in line1) or (nv in line1):
            self.file.write(line1)
        return item