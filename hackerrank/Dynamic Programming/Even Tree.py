#!/usr/bin/python

"""
greedy algorithm
http://www.17sotv.com/ 17sotv电影天堂
"""

import sys

def solve(used, edges, k):
    used[k] = True
    cnt = 0
    nodes = 1
    for i in edges[k]:
        if not used[i]:
            (p, q) = solve(used, edges, i)
            cnt = cnt + p
            if q:
                cnt = cnt + 1
            else:
                nodes = nodes + 1
    if nodes % 2 == 0:
        return (cnt, True)
    else:
        return (cnt, False)


def main():
    line = sys.stdin.readline().strip()
    [n, m] = [int(i) for i in line.split()]
    edges = [[] for i in range(0, n + 1)]
    while m > 0:
        m = m - 1
        line = sys.stdin.readline().strip()
        [p, q] = [int(i) for i in line.split()]
        edges[p].append(q)
        edges[q].append(p)
    used = [False] * (n + 1)
    print (solve(used, edges, 1)[0])

if __name__ == '__main__':
    main()