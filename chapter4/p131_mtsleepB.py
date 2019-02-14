#!/usr/bin/env python3

import _thread
import time


def loop(nloop, nsec, lock):
    print("start loop {} at: {}".format(nloop, time.ctime()))
    time.sleep(nsec)
    print("loop {} done at: {}".format(nloop, time.ctime()))
    lock.release()


def main():
    loops = [4, 2]
    print("starting at: {}".format(time.ctime()))
    # 创建锁列表
    locks = []
    for i in range(len(loops)):
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    # 派生线程
    for i in range(len(loops)):
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))
    # 等待线程结束
    for i in range(len(loops)):
        locks[i].acquire()
        locks[i].release()
    print("all DONE at: {}".format(time.ctime()))


if __name__ == "__main__":
    main()
