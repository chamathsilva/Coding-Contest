__author__ = 'chamathsilva'

from collections import Counter
import string

counter1 = Counter(list(input()))
counter2 = Counter(list(input()))

deletions = 0
for i in string.ascii_lowercase:
    deletions += abs(counter1[i]-counter2[i])

print(deletions)