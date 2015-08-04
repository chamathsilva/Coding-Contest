__author__ = 'chamathsilva'

for i in range(int(input())):
    N, K = input().split()
    K = int(K)
    temp = [int(i) for i in input().split()]

    present_count = 0
    for j in temp:
        if j <= 0:
            present_count += 1

    if K > present_count:
        print("YES")
    else:
        print("NO")
