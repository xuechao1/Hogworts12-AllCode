#!/usr/bin/env python
# -*- coding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/9/5 21:19'

_params = {"name": "12345"}
str = "xxxxxxxx ${name}lllllllllllll"
for key, value in _params.items():
    print("key : ", key)
    print("value : ", value)
    str = str.replace(f'${{{key}}}', value)
    print(str)
