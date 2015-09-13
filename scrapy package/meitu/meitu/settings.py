# -*- coding: utf-8 -*-

# Scrapy settings for meitu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'meitu'

SPIDER_MODULES = ['meitu.spiders']
NEWSPIDER_MODULE = 'meitu.spiders'

ITEM_PIPELINES = ['meitu.pipelines.MeituPipeline']  # ImagePipeline的自定义实现类
IMAGES_STORE = 'D:\\test_pic'   # 图片存储路径
IMAGES_EXPIRES = 90                                   # 过期天数
IMAGES_MIN_HEIGHT = 100                               # 图片的最小高度
IMAGES_MIN_WIDTH = 100                                # 图片的最小宽度

