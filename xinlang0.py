# -*- coding = utf-8 -*-
# @Time : 2021/3/9 11:08
# @Author : 凹凸由
# @File ：xinlang0.py
from pyquery import PyQuery as pq
import requests
from fake_headers import Headers
from loguru import logger
import time
from selenium import webdriver


# fetch
def fetch(url, **kwargs):
    try:
        headers = Headers(headers=True).generate()
        # kwargs.setdefault('timeout', 10)
        # kwargs.setdefault('verify', False)
        kwargs.setdefault('headers', headers)
        # headers = {
        #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
        # }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
    except requests.ConnectionError:
        return


# parse
def parse(html):
    return
    # browser = webdriver.Chrome
    # browser.get("https://www.baidu.com/")
    # time.sleep(1)
    # browser.refresh()
    # js = "document.getElementsById('d_list').style.display='block'"
    # html = browser.find_element_by_xpath("//div[@id='d_list']/preceding-sibling::div[1]")
    # print(html)
    # browser.execute_script(js)
    # print(driver)
    # doc = pq(html)
    # items = doc('a')
    # print(items)
    # exit()
    # for item in items:
    #     print(item)
    # href = item.attr.href
    # selenium crawler


def test():
    html = '''
    <html>
        <head>
            <title>Hello PyQuery</title>
        </head>
        <body>
            <ul id="container">
                <li class="l1">l1</li>
                <li class="l2">l2</li>
                <li class="l3">l3</li>
            </ul>
        </body>
    </html>
    '''
    doc = pq(html)
    lis = doc('li').items()
    print(lis)
    # 获取第二个 li
    l2 = list(lis)[1]
    print(l2)


def browser():
    driver = webdriver.Chrome()
    driver.get("https://news.sina.com.cn/roll")
    time.sleep(2)
    dom = driver.find_element_by_id('d_list')
    html = dom.get_attribute('innerHTML')
    # pyquery接受字符串
    doc = pq(html)
    items = doc('ul a').items()
    for item in list(items):
        print(item.attr('href'))
    #退出
    driver.quit()

if __name__ == '__main__':
    url = 'https://news.sina.com.cn/roll'
    browser()
    # test()
