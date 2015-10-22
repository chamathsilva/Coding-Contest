__author__ = 'chamathsilva'

graph = {}
edge = []

class Node(object):
    def __init__(self):
        self.color = 'white'
        self.parent = None
        self.distance = -1
        self.adj = []

    def __repr__(self):
        return "color :" + str(self.color) + " adj:" + str(self.adj) + "distance:" + str(self.distance)

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()



def graph_maker(no_of_node, edge_list):
    global graph
    for k in range(1, no_of_node+1):
        graph[str(k)] = Node()
    for u, v in edge_list:
        graph[u].adj.append(v)
        graph[v].adj.append(u)
    for k in range(1, no_of_node+1):
        graph[str(k)].adj = set(graph[str(k)].adj)




def bfs(Graph, S):
    start = Graph[str(S)]
    start.patent = None
    start.distance = 0
    Q = Queue()
    Q.enqueue(start)

    while not Q.isEmpty():
        current = Q.dequeue()
        for nbr in current.adj:
            nbrNode = Graph[nbr]
            if nbrNode.color == "white":
                nbrNode.color = "gray"
                nbrNode.distance = current.distance + 1
                nbrNode.parent = current
                Q.enqueue(nbrNode)
        current.color = "black"





def finder():
    global N
    global start
    global graph
    for i in range(1, N+1):
        if str(i) == start:
            continue
        else:
            dis = graph[str(i)].distance
            if dis != -1:
                print(dis * 6, end=" ")
            else:
                print(dis, end=" ")
    print("")


for z in range(int(input())):
    graph = {}
    edge = []
    N, M = map(int, input().split())
    for _ in range(M):
        edge.append(tuple(input().split()))
    start = input()


    graph_maker(N,edge)
    bfs(graph,start)
    finder()