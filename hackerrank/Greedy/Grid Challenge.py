__author__ = 'chamathsilva'

for _ in range (int(input())):
    N = int(input())
    grid = [list(input()) for i in range(N)]
    index = 1
    grid[0].sort()
    while index < N:
        grid[index].sort()
        for i in range(N):
            if grid[index-1][i] > grid[index][i]:
                index = float("inf")
                break
        index += 1

    print(["NO", "YES"][index == N])



