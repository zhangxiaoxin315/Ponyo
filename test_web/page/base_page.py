#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
#@Time      :2021/8/2 22:41
#@Author    :xiaoxin
#@File      :base_page.py
'''
from selenium import webdriver


class Page(object):

    def __init__(self,driver,base_url='https://m.myweimai.com/account/login.html'):
        self.driver = driver
        self.url = base_url

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def input_text(self,loc,text):
        self.find_element(*loc).send_keys(text)

    def click(self,loc):
        self.find_element(*loc).click()

    def get_title(self):
        return self.driver.title

    # def mobile_web(self):
    #     self.mobileEmulation = {"device":"iPhone X"}
    #     self.options = webdriver.ChromeOptions()
    #     self.options.add_argument('--headless')
    #     self.options.add_experimental_option('mobileEmulation',self.mobileEmulation)
    #     self.driver = webdriver.Chrome(options=self.options)