# -*- coding = utf-8 -*-
# @Time : 2021/3/10 14:39
# @Author : 凹凸由
# @File ：qqnews.py


import requests
import re
from selenium import webdriver
import time

def search():
    browser = webdriver.Chrome()
    # browser = webdriver.PhantomJS()
    # browser.set_window_size(1920,1080)
    browser.get("https://news.qq.com/")
    # element = browser.find_element_by_id('load-more')
    # browser.execute_script("arguments[0].scrollIntoView();", element)

    # try:
    #     element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "search-show"))
    #     )
    #     element.click()
    # finally:
    #     time.sleep(10)
    #     driver.quit()

    browser.execute_script("window.scrollTo(0,10000)")
    time.sleep(3)
    browser.execute_script("window.scrollTo(0,10000)")
    time.sleep(3)
    html = browser.page_source

    #parse
    # hrefs = re.findall(r'<a href="(.*?.html)">',html)
    hrefs = re.findall(r'<a class="picture" href="(.*?.html)"',html)
    browser.quit()
    return hrefs
if __name__ == '__main__':
    print(search())
