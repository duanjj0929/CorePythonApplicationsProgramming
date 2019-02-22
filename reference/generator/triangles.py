#!/usr/bin/env python3

# 杨辉三角定义如下：
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1


def triangles():
    ret = [1]
    while True:
        yield ret
        ret = [sum(x) for x in zip([0] + ret, ret + [0])]


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
def _main():
    n = 0
    results = []
    for t in triangles():
        print(t)
        results.append(t)
        n = n + 1
        if n >= 10:
            break
    if results == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1],
                   [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1],
                   [1, 7, 21, 35, 35, 21, 7, 1],
                   [1, 8, 28, 56, 70, 56, 28, 8, 1],
                   [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]:
        print('测试通过!')
    else:
        print('测试失败!')


if __name__ == "__main__":
    _main()
