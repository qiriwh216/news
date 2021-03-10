# -*- coding = utf-8 -*-
# @Time : 2021/3/9 15:37
# @Author : 凹凸由
# @File ：wangyi0.py
from pyquery import PyQuery as pq
import re
import requests
from selenium import webdriver
import time
from lxml import etree
# ndi_main


def getHtml():

    urls = [
       'https://news.163.com/'
    ]
    headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    }

    for url in urls:
        try:
            response = requests.get(url,headers=headers)
            if response.status_code == 200:
                response.encoding = 'gbk'
                return response.text
        except requests.ConnectionError:
            return

    #parse
def parse(html):
    # print(html)
    # exit()
    # doc = pq(html)
    # items = doc('div.ndi_main a').items()
    # for item in items:
    #     print(item.attr('href'))
    # re.compile(r'<a href="(.*?).html">')
    # (r'<a href="(.*?)">')
    doc = pq(html)
    # html = doc('.main_center_news').html()
    html = doc('.newsdata_list').html()
    # html = doc('.ndi_main').html()
    # htmlX = re.findall(r'<div class="hidden">(.*?)</div>',html)
    # print(htmlX)
    # exit()
    hrefs = re.findall(r'<a href="(.*?.html)">',html)
    links = []
    for href in hrefs:
        # links.append(href+'.html')
        links.append(href)
    return len(links)

def parseX(html):
    doc = etree.HTML(html)
    html = doc.xpath('//div[class="hidden"]/following-sibling::*')
    print(html)
    # result = etree.tostring(html, pretty_print=True)
    # html = etree.parse(path,etree.HTMLParser())
    # result = etree.tostring(html)
    # print(result.decode('utf-8'))
    # < div class ="hidden" ne- if ="{{__i == 0}}" >

def  browser():
    driver = webdriver.Chrome()
    driver.get("https://news.163.com/")
    driver.maximize_window()
    driver.implicitly_wait(3)
    dom = driver.find_element_by_id('d_list')
    page = dom.get_attribute('innerHTML')
    # page = driver.page_source
    print(page)
    # dom = driver.find_element_by_id('d_list')
    # html = dom.get_attribute('innerHTML')
    # pyquery接受字符串
    # doc = pq(html)
    # items = doc('ul a').items()
    # for item in list(items):
    #     print(item.attr('href'))
    #退出
    driver.quit()






if __name__ == '__main__':
    d = getHtml()
    data = parse(d)
    print(data)
    # print(data)
    # browser()