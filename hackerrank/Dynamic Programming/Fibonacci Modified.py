__author__ = 'chamathsilva'

A, B, N = map(int,input().split())

memo = [A, B]
index = N-1
for i in range (2,N):
    memo.append((memo[i-1])**2 + memo[i-2])
print(memo[index])
