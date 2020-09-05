#!/usr/bin/env python
# -*- coding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/9/5 10:49'

from ui_framework_demo.page.app import App


class TestBase:
    app = None

    def setup(self):
        self.app = App()
