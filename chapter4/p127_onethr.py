#!/usr/bin/env python3

import time


def loop0():
    print("start loop 0 at: {}".format(time.ctime()))
    time.sleep(4)
    print("loop 0 done at: {}".format(time.ctime()))


def loop1():
    print("start loop 1 at: {}".format(time.ctime()))
    time.sleep(2)
    print("loop 1 done at: {}".format(time.ctime()))


def main():
    print("starting at: {}".format(time.ctime()))
    loop0()
    loop1()
    print("all DONE at: {}".format(time.ctime()))


if __name__ == "__main__":
    main()
