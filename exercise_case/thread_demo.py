#!/usr/bin/env python
# -*- coding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/8/31 9:06'

import _thread
import logging
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)  # logging初始化，设置打印的日志级别


def loop0():
    # ctime 打印当前时间
    logging.info("start loop0 at" + ctime())
    sleep(2)
    logging.info("end loop0 at" + ctime())


def loop1():
    # ctime 打印当前时间
    logging.info("start loop1 at" + ctime())
    sleep(2)
    logging.info("end loop1 at" + ctime())


def main():
    logging.info("start all at " + ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(4)
    logging.info("start end at" + ctime())


if __name__ == '__main__':
    main()
