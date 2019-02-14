#!/usr/bin/env python3

from p139_myThread import MyThread
import time


def fib(x):
    time.sleep(0.005)
    if x < 2:
        return (1)
    else:
        return (fib(x - 2) + fib(x - 1))


def fac(x):
    time.sleep(0.1)
    if x < 2:
        return (1)
    else:
        return (x * fac(x - 1))


def sum(x):
    time.sleep(0.1)
    if x < 2:
        return (1)
    else:
        return (x + sum(x - 1))


funcs = [fib, fac, sum]
n = 12


def main():
    print("*** SINGLE THREAD")
    for func in funcs:
        print("starting {} at: {}".format(func.__name__, time.ctime()))
        print("{}({}) = {}".format(func.__name__, n, func(n)))
        print("{} finished at: {}".format(func.__name__, time.ctime()))

    print("\n*** MULTIPLE THREADS")
    threads = []
    for func in funcs:
        t = MyThread(func, (n, ), func.__name__)
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
        print("{}({}) = {}".format(t.func.__name__, n, t.getResult()))


if __name__ == "__main__":
    main()
