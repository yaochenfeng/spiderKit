# -*- coding: utf-8 -*-
import scrapy


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['http://lagou.com/']
    # 自定义setting
    custom_settings = {
        'SOME_SETTING': 'some value',
    }
    def parse(self, response):
        pass
