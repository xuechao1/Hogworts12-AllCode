#!/usr/bin/env python
# -*- coding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/9/2 18:19'

from test_selenium.test_wework_login.login import Login
from test_selenium.test_wework_login.register import Register


class Index:

    def goto_login(self):
        # click login
        return Login()

    def goto_register(self):
        # click register
        return Register()
