#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 汉诺塔


def hanoi(n, a, b, c):
    if 1 == n:
        print("{} --> {}".format(a, c))
    else:
        hanoi(n - 1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n - 1, b, a, c)


# 调用
hanoi(3, 'A', 'B', 'C')
