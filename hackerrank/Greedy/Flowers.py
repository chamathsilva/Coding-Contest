__author__ = 'chamathsilva'

N, K = map(int, input().split())
flowers = sorted(map(int,input().split()),reverse=True)

amount = 0
x = 1
status = 0
for i in flowers:
    if status == K:
        x += 1
        status = 0
    amount += x * i
    status += 1

print(amount)