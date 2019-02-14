#!/usr/bin/env python3

from atexit import register
from random import randrange
from threading import Thread, Lock, current_thread
from time import sleep, ctime


class CleanOutputSet(set):
    def __str__(self):
        return ", ".join(sorted(self))


lock = Lock()
loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = CleanOutputSet()


def loop(nsec):
    myname = current_thread().name
    with lock:
        remaining.add(myname)
        print("[{}] Started {}".format(ctime(), myname))
    sleep(nsec)
    with lock:
        remaining.remove(myname)
        print("[{}] Completed {} ({} secs)".format(ctime(), myname, nsec))
        print("\t(remaining: {})".format(remaining or "NONE"))


def _main():
    for pause in loops:
        Thread(target=loop, args=(pause, )).start()


@register
def _atexit():
    print("all DONE at: {}".format(ctime()))


if __name__ == "__main__":
    _main()
