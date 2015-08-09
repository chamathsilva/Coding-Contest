__author__ = 'chamathsilva'

N = input()
toys = list(sorted(set(map(int, input().split()))))
count = 0
while len(toys) > 0:
    start = toys[0]
    #toys = [i for i in toys if not (start <= i <= start + 4)]
    for i in range (start+4,start-1,-1):
        if i in toys:
            toys = toys[toys.index(i)+1:]
            print(toys)
            break
    count += 1

print(count)