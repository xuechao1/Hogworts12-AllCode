#!/usr/bin/env python
# -*- coding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/9/2 12:21'

from exercise_case.pageObject.main import Main


class TestPageObject:

    # page_object 举例
    def test_demo(self):
        main = Main()
        # click_first_link 是 Main.py上的函数方法
        # get_text  是  click_first_link 方法中return跳转到 hogworts中的get_text方法
        main.click_first_link().get_text()
