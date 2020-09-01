#!/usr/bin/env python
# -*- coding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/8/31 9:25'

import logging
import threading
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)
loops = [2, 4]

"""
进阶学习，必须会的知识点
原语-----》核心：多个线程可以访问同一个数据；但是一定会造成数据的错误
原语子概念---锁概念（原语用锁，解决了数据的互斥访问--数据只允许一个线程访问）
        ----信号量（比锁更加灵活，锁是True或False，信号量可以是0，1，2，3各种值）
"""


class MyThread(threading.Thread):

    def __init__(self, func, args, name=""):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.run(*self.args)


def loop(nloop, nesc):
    logging.info("start loop " + str(nloop) + "at" + ctime())
    sleep(nesc)
    logging.info("end loop " + str(nloop) + "at" + ctime())


def main():
    logging.info("start all at " + ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at " + ctime())


if __name__ == '__main__':
    main()

"""
进阶学习，必须会的知识点
原语-----》核心：多个线程可以访问同一个数据；但是一定会造成数据的错误
原语子概念---锁概念（原语用锁，解决了数据的互斥访问--数据只允许一个线程访问）
        ----信号量（比锁更加灵活，锁是True或False，信号量可以是0，1，2，3各种值）
"""
