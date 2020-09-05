#!/usr/bin/env python
# -*- coding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/9/3 19:25'

import itertools

a = [1, 2, 3]
b = [4, 5, 6]
c = [1, 2, 3]
d = [4, 5, 6]
for x in itertools.product(a, b, c, d):
    print(x)
