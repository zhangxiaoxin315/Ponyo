#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
#@Time      :2021/8/2 22:42
#@Author    :xiaoxin
#@File      :login_page.py
'''
from selenium.webdriver.common.by import By
from test_web.page.base_page import Page

class Login_page(Page):

    password_login_button = (By.CLASS_NAME,'toggleMode')
    phone_input = (By.CLASS_NAME,'phone')
    password_input = (By.CLASS_NAME,'password')
    login_button = (By.CLASS_NAME,'login')
    agree_button = (By.CLASS_NAME,'am-checkbox-input')

    def __init__(self,driver,base_url='https://m.myweimai.com/account/login.html'):
        Page.__init__(self,driver,base_url)

    def gotoWeimaiLogin(self):
        self.driver.get(self.url)

    def switch_password_login(self):
        self.click(self.password_login_button)

    def input_phone(self,text):
        self.input_text(self.phone_input,text)

    def input_password(self,text):
        self.input_text(self.password_input,text)

    def click_login(self):
        self.click(self.login_button)

    def click_agree(self):
        self.click(self.agree_button)