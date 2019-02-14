#!/usr/bin/env python3

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, func, args, threadName=""):
        super().__init__(name=threadName)
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print("starting {} at: {}".format(self.name, time.ctime()))
        self.res = self.func(*self.args)
        print("{} finished at: {}".format(self.name, time.ctime()))


if __name__ == "__main__":
    t = MyThread(max, (1, 2), max.__name__)
    t.start()
    t.join()
    print(t.getResult())
