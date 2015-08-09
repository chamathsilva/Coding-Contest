__author__ = 'chamathsilva'

N,K = map(int, input().split())
number = list(map(int, input().split()))

indexx = 0
exchange = 0
while exchange < K:
    max_index = number.index(max(number[indexx:]))
    if max_index != indexx:
        (number[indexx], number[max_index]) = (number[max_index], number[indexx])
        exchange += 1

    indexx += 1
    if indexx == N:
        break

print(' '.join(map(str, number)))


