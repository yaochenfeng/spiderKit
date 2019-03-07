# -*- coding: utf-8 -*-
import scrapy
import json
import logging

'''
优选智投 https://www.weidai.com.cn/list/goodsList?type=0&periodType=0&page=1&rows=10&goodsType=PACKAGE
散标列表 https://www.weidai.com.cn/list/goodsList?type=0&periodType=0&sort=0&page=1&rows=10&goodsType=BIDDING
'''
class WeidaiapiSpider(scrapy.Spider):
    name = 'weidaiapi'
    allowed_domains = ['www.weidai.com.cn']
    start_urls = ['https://www.weidai.com.cn/list/goodsList']

    def parse(self, response):
        logging.info("res")
        logging.info(response.body)
        # 返回的是json数据
        # 转换为python中的字典
        rs = json.loads(response.text)
        if rs.get('success') == 'success':
            # 取出数据
            data = rs.get('data')
            pageIndex = rs.get('pageIndex')#第几页
            count = rs.get('count')#总共多少条

