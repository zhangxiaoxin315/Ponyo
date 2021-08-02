#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
#@Time      :2021/8/2 23:55
#@Author    :xiaoxin
#@File      :test_login.py
'''
import pytest
from test_web.page.login_page import Login_page
from selenium import webdriver
import time
class TestWeimaiLogin():

    def setup_method(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver
        phone = '13750832021'
        password = '000000'
        url = 'https://m.myweimai.com/account/login.html'
        login_Page = Login_page(driver,url)
        login_Page.gotoWeimaiLogin()
        login_Page.switch_password_login()
        login_Page.input_phone(phone)
        login_Page.input_password(password)
        login_Page.click_agree()
        login_Page.click_login()
        time.sleep(2)

        assert login_Page.get_title() =="个人中心"
    def teardown_method(self):
        self.driver.quit()