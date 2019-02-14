#!/usr/bin/env python3

import multiprocessing
import random
import time


def worker(q):
    while True:
        item = q.get()
        if item is None:
            break
        print("{}({}) do work with {}".format(
            multiprocessing.current_process().name,
            multiprocessing.current_process().pid, item))
        time.sleep(random.randint(1, 3))
        q.task_done()


work_queue = multiprocessing.JoinableQueue()

processes = []
num_worker_processes = random.randint(1, 5)
for i in range(num_worker_processes):
    p = multiprocessing.Process(
        target=worker, name="Process-{}".format(i), args=(work_queue, ))
    processes.append(p)

for p in processes:
    p.start()

item_list = (x for x in range(2 * num_worker_processes))
for item in item_list:
    work_queue.put(item)

# block until all tasks are done
work_queue.join()

# stop workers
for i in range(num_worker_processes):
    work_queue.put(None)
for p in processes:
    p.join()

print("Parent Process {}({}) DONE.".format(
    multiprocessing.current_process().name,
    multiprocessing.current_process().pid))
