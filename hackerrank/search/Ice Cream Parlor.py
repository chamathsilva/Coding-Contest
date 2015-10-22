__author__ = 'chamathsilva'

from collections import Counter

for _ in range(int(input())):
    M = int(input())
    N = int(input())
    string = list(map(int, input().split()))
    flavors = Counter(sorted(string))
    for i in flavors:
        nextt = M - i
        if nextt in flavors.keys():
            if nextt != i:
                print(' '.join(map(str,sorted([string.index(i)+1, string.index(nextt)+1]))))
                break
            if nextt == i:
                if flavors[nextt] > 1:
                    index1 = string.index(i)
                    string.remove(i)
                    index2 = string.index(i)
                    print(index1+1, index2+2)
                    break
