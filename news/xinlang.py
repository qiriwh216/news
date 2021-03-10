# -*- coding = utf-8 -*-
# @Time : 2021/3/9 10:34
# @Author : 凹凸由
# @File ：xinlang.py
from pyquery import  PyQuery as pq
from base import BaseCrawler
from loguru import logger

BASE_URL = 'https://news.sina.com.cn/roll'

class DdtaXLCrawler(BaseCrawler):
    urls = [BASE_URL]
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }

    @logger.catch
    def crawl(self):
        """
        crawl main method
        """
        for url in self.urls:
            logger.info(f'fetching {url}')
            html = self.fetch(url, headers=self.headers)
            for proxy in self.parse(html):
                logger.info(f'fetched proxy {proxy.string()} from {url}')
                yield proxy

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = pq(html)
        items = doc('div#d_list a').items()
        print(items)
        for item in items:
            href = item.attr.href
            # yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = DdtaXLCrawler()
    for proxy in crawler.crawl():
        print(proxy)
