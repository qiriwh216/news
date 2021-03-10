# -*- coding = utf-8 -*-
# @Time : 2021/3/10 16:32
# @Author : 凹凸由
# @File ：zhongxin0.py
import requests
import re


def get_doc():
    # urls = ['https://news.ifeng.com/']
    urls = ['https://www.chinanews.com/scroll-news/news1.html']
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }
    for url in urls:
        try:
            response = requests.get(url,headers=headers)
            if response.status_code == 200:
                response.encoding = 'utf-8'
                return response.text
        except requests.ConnectionError:
            return
def parse(doc):
    dataList = []
    hrefs = re.findall(r'<a class="news-stream-newsStream-image-link" href="(.*?)"',doc)
    for href in hrefs:
        dataList.append('https:'+href)
    return dataList

if __name__ == '__main__':
    d = get_doc()
    p = parse(d)
    print(d)
