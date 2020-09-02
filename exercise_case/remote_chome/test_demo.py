#!/usr/bin/env python
# -*- coding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/9/2 16:04'

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        #self.driver.get("https://ceshiren.com/")
        self.driver.find_element(By.ID, 'menu_contacts').click()
        sleep(5)

