#!/usr/bin/env python
# -*- coding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/8/29 21:00'

import time

"""
获取3天后的时间
"""
now_time = time.time()
three_days_time = now_time + 60*60*24*3
time_tuple = time.localtime(three_days_time)
print(time.strftime("%Y-%m-%d %H:%M:%S", time_tuple))
