import heapq

#Q=[(11, 'z'),(3, 'v')]

Q = []

heapq.heappush(Q,(133,'A'))
heapq.heappush(Q,(33,'Z'))
heapq.heappush(Q,(133,'A'))
heapq.heappush(Q,(-1,'Z'))

print(heapq.heappop(Q))
print(Q)
print(heapq.heappop(Q))
print(Q)

class Node(object):
    def __init__(self):
        self.color = 'white'
        self.parent = None
        self.distance = -1
        self.adj = []

    def __repr__(self):
        return "color :" + str(self.color) + " adj:" + str(self.adj) + "distance:" + str(self.distance)

    def __lt__(self, other):
        return self.distance < other.distance


x = Node()

x.distance = 34
x.color = 'red'

y = Node()
y.distance = 36
y.color = "black"


R = []
heapq.heappush(R, x)
heapq.heappush(R, y)

print(R)

print(heapq.heappop(R))
#print(R)
print(heapq.heappop(R))
#print(R)

test = [x, y]

print(sorted(test))

tt = {'a':12,'b':22,'c':33}
print(tt)

for i in tt:
    print(i)
    print(tt[i])