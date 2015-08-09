__author__ = 'chamathsilva'

import math

for _ in range(int(input())):
    A, B = map(int,input().split())

    count = 0
    current = math.ceil(math.sqrt(A))
    while current**2 <= B:
        count += 1
        current += 1


    print(count)


'''

method 2

    print (math.floor(math.sqrt()) - math.ceil(math.sqrt())) + 1

'''