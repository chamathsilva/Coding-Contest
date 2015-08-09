__author__ = 'chamathsilva'

for i in range(int(input())):
    print(["NO", "YES"][set(input()).intersection(set(input())) != set()])