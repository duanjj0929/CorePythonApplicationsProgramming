#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 埃拉托色尼筛选法
# （1）先把1删除（现今数学界1既不是质数也不是合数）
# （2）读取队列中当前最小的数2，然后把2的倍数删去
# （3）读取队列中当前最小的数3，然后把3的倍数删去
# （4）读取队列中当前最小的数5，然后把5的倍数删去
# （5）读取队列中当前最小的数7，然后把7的倍数删去
# （6）如上所述直到需求的范围内所有的数均删除或读取


# 生成器生成从3开始的无限奇数序列
def _int_iter():
    n = 3
    while True:
        yield n
        n += 2


# 定义筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2  # 先返回一个2
    it = _int_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


def _main():
    # 构造循环条件，使之可以输出任何范围的素数序列
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break


if __name__ == "__main__":
    _main()
