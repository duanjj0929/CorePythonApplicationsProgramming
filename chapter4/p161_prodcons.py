#!/usr/bin/env python3

from random import randint
from time import sleep
from queue import Queue
from p139_myThread import MyThread


def writeQ(q):
    item = randint(1, 100)
    print("producing {} for Q...".format(item), end="")
    q.put(item)
    print("size now {}".format(q.qsize()))


def readQ(q):
    val = q.get()
    print("consumed {} from Q... size now {}".format(val, q.qsize()))
    q.task_done()


def writer(q, loops):
    for i in range(loops):
        writeQ(q)
        sleep(randint(1, 3))


def reader(q, loops):
    for i in range(loops):
        readQ(q)
        sleep(randint(2, 5))


funcs = [writer, reader]


def _main():
    nloops = randint(2, 5)
    q = Queue(32)

    threads = []
    for f in funcs:
        t = MyThread(func=f, args=(q, nloops), threadName=f.__name__)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("all DONE")


if __name__ == "__main__":
    _main()
