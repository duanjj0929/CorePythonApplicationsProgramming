#!/usr/bin/env python3
# -*- coding: utf-8 -*-

INF = float('inf')  # 用inf(infinity的缩写)存储一个我们认为的正无穷值


def dijkstra(graph, src):
    # 访问过的点
    visited = [src]
    # 未访问过的点
    nodes = [i for i in range(len(graph)) if i != src]
    # 初始化dis数组，这里是SRC号顶点到其余各个顶点的初始路程
    dis = [graph[src][i] for i in nodes]
    dis.insert(src, graph[src][src])

    while nodes:
        min_dis = INF
        for i in nodes:
            if dis[i] < min_dis:
                min_dis = dis[i]
                u = i
        visited.append(u)
        nodes.remove(u)
        for i in nodes:
            mid_dis = dis[u] + graph[u][i]
            if mid_dis < dis[i]:
                dis[i] = mid_dis
    return dis


def _main():
    GRAPH = [[0, 1, 12, INF, INF, INF], [INF, 0, 9, 3, INF, INF],
             [INF, INF, 0, INF, 5, INF], [INF, INF, 4, 0, 13, 15],
             [INF, INF, INF, INF, 0, 4], [INF, INF, INF, INF, INF, 0]]
    SRC = 0
    print(dijkstra(GRAPH, SRC))


if __name__ == "__main__":
    _main()
