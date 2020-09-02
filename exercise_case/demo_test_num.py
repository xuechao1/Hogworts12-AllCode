#!/usr/bin/env python
# -*- coding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/8/29 11:18'

import random

computer_num = random.randint(1, 100)
while True:
    guess_num = int(input("请输入一个数字： "))
    if guess_num < computer_num:
        print("samll")
    elif guess_num > computer_num:
        print("big")
    elif guess_num == computer_num:
        print(" you are right")
        break
