__author__ = 'chamathsilva'


N = int(input())
orders = sorted([(i, sum(map(int, input().split()))) for i in range(1, N+1)], key=lambda x: x[1])
for i in orders:
    print(i[0], end=' ')