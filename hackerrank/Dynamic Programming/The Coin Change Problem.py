__author__ = 'chamathsilva'

N, M = map(int,input().split())
coin = list(map(int,input().split()))

memo = [[0 for i in range (N+1)] for _ in range(M+1)]
memo[0][0] = 1


for i in range(1, M+1):
    for j in range(1, N+1):
        yet_no_way = memo[i-1][j]
        memo[i][j] = yet_no_way

        if j == coin[i-1]:
            memo[i][j] += 1
        elif j > coin[i-1]:
            left = j - coin[i-1]
            memo[i][j] += memo[i][left]

for i in memo:
    print(i)
print(memo[-1][-1])