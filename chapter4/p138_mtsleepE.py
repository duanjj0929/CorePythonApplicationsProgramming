#!/usr/bin/env python3

import threading
import time

loops = [4, 2]


class MyThread(threading.Thread):
    def __init__(self, func, args, threadName=""):
        super().__init__(name=threadName)
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print("start loop {} at: {}".format(nloop, time.ctime()))
    time.sleep(nsec)
    print("loop {} done at: {}".format(nloop, time.ctime()))


def main():
    print("starting at: {}".format(time.ctime()))
    # create all threads
    threads = []
    for i in range(len(loops)):
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)
    # start thread
    for t in threads:
        t.start()
    # wait for all threads to finish
    for t in threads:
        t.join()
    print("all DONE at: {}".format(time.ctime()))


if __name__ == "__main__":
    main()
