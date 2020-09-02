#!/usr/bin/env python
# -*- coding: utf-8 -*-
___author___ = 'Steven Emerson'
___date___ = '2020/8/31 9:25'

import logging
import threading
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)
loops = [2, 4]


def loop(nloop, nesc):
    logging.info("start loop " + str(nloop) + "at" + ctime())
    sleep(nesc)
    logging.info("end loop " + str(nloop) + "at" + ctime())


def main():
    logging.info("start all at " + ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loop[i]))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at " + ctime())


if __name__ == '__main__':
    main()
