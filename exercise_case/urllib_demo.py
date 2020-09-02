#!/usr/bin/env python
# -*- coding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/8/29 21:10'

import urllib.request
from pprint import pprint

res = urllib.request.urlopen("https://www.baidu.com")
print(res.status)
pprint(res.read())
print(res.headers)
