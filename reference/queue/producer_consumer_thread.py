#!/usr/bin/env python3

# https://docs.python.org/3/library/queue.html

import queue
import random
import threading


def worker():
    while True:
        item = q.get()
        if item is None:
            break
        print("{} do work with {}".format(threading.current_thread().name,
                                          item))
        q.task_done()


q = queue.Queue()

threads = []
num_worker_threads = random.randint(1, 5)
for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    threads.append(t)

for t in threads:
    t.start()

item_list = (x * x for x in range(2 * num_worker_threads))
for item in item_list:
    q.put(item)

# block until all tasks are done
q.join()

# stop workers
for i in range(num_worker_threads):
    q.put(None)
for t in threads:
    t.join()
