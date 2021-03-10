# -*- coding = utf-8 -*-
# @Time : 2021/3/9 09:00
# @Author : 凹凸由
# @File ：test.py
import json
from pyquery import PyQuery as pq

class Proxy(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k,v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawFunc__'].append(k)
                count += 1
        attrs['__CrawFunc__'] = count
        return type.__new__(cls, name, bases, attrs)

class Crawler(object,metaclass=Proxy):
    def get_proxies(self,callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print('成功获取到代理',proxy)
            proxies.append(proxy)
        return proxies

    def crawl_daili666(self,page_count=4):
        """
        获取代理66
        :param page_count: 页码
        :return: 代理
        """
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1,page_count+1)]
        for url in urls:
            print('Crawling', url)
            html = get_page(url)
            if html:
                doc = pq(html)
                lines = doc('div[name="list_proxy_ip"]').items()
                for line in lines:
                    ip = line.find('.tbBottomLine:nth-child(1)').text()
                    port = line.find('.tbBottomLine:nth-child(2)').text()
                    yield  ':'.join([ip,port])