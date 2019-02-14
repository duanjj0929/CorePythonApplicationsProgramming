#!/usr/bin/env python3

import _thread
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
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    time.sleep(6)
    print("all DONE at: {}".format(time.ctime()))


if __name__ == "__main__":
    main()
