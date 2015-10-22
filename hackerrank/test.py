__author__ = 'chamathsilva'
__author__ = 'chamathsilva'

from collections import defaultdict

import heapq


def prim(S, N, G):
    E    = defaultdict(int)
    D    = {}
    T    = [0 for _ in range(N + 1)]
    H    = [(0, S)]

    for n in range(1, N + 1):
        D[n] = float('inf')

    D[S] = 0

    while H:
        t = heapq.heappop(H)
        for h in G[t[1]]:
            if E[h[1]] == 0 and D[h[1]] > h[0]:
                D[h[1]] = h[0]
                if h in H:
                    H.remove(h)
                    heapq.heapify(H)
                heapq.heappush(H, (D[h[1]], h[1]))
                T[h[1]] = D[h[1]]
            E[t[1]] += 1
    print(E)
    print(D)
    print(T)

    return T


def main():
    N, M = [int(i) for i in input().split()]

    G    = defaultdict(set)

    for _ in range(M):
        e = [int(i) for i in input().split()]
        G[e[0]].add((e[2], e[1]))
        G[e[1]].add((e[2], e[0]))

    S    = int(input())

    #print(G)

    print(sum(prim(S, N, G)))


if __name__ == "__main__":
    main()