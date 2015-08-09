__author__ = 'chamathsilva'

from collections import Counter
import string

for _ in range(int(input())):
    stringmain = input()
    N = len(stringmain)
    if N % 2 == 1:
        print(-1)
    else:
        N /= 2
        N = int(N)
        counter1 = Counter(stringmain[:N])
        counter2 = Counter(stringmain[N:])

        same_characters = 0
        for i in string.ascii_lowercase:
            same_characters += min(counter1[i], counter2[i])

        print(N - same_characters)
