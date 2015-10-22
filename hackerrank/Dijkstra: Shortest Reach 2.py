
from __future__ import generators

class priorityDictionary(dict):

    def __init__(self):
        self.__heap = []
        dict.__init__(self)

    def smallest(self):
        if len(self) == 0:
            raise IndexError("smallest of empty priorityDictionary")
        heap = self.__heap
        while heap[0][1] not in self or self[heap[0][1]] != heap[0][0]:
            lastItem = heap.pop()
            insertionPoint = 0
            while 1:
                smallChild = 2*insertionPoint+1
                if smallChild+1 < len(heap) and \
                        heap[smallChild] > heap[smallChild+1]:
                    smallChild += 1
                if smallChild >= len(heap) or lastItem <= heap[smallChild]:
                    heap[insertionPoint] = lastItem
                    break
                heap[insertionPoint] = heap[smallChild]
                insertionPoint = smallChild
        return heap[0][1]

    def __iter__(self):
        def iterfn():
            while len(self) > 0:
                x = self.smallest()
                yield x
                del self[x]
        return iterfn()

    def __setitem__(self,key,val):
        dict.__setitem__(self,key,val)
        heap = self.__heap
        if len(heap) > 2 * len(self):
            self.__heap = [(v,k) for k,v in self.iteritems()]
            self.__heap.sort()
        else:
            newPair = (val,key)
            insertionPoint = len(heap)
            heap.append(None)
            while insertionPoint > 0 and \
                    newPair < heap[(insertionPoint-1)//2]:
                heap[insertionPoint] = heap[(insertionPoint-1)//2]
                insertionPoint = (insertionPoint-1)//2
            heap[insertionPoint] = newPair

    def setdefault(self,key,val):
        if key not in self:
            self[key] = val
        return self[key]



#########################

def Dijkstra(G, start, end=None):
    D = {}
    P = {}
    Q = priorityDictionary()
    Q[start] = 0

    for v in Q:
        D[v] = Q[v]
        if v == end: break

        for w in G[v]:
            vwLength = D[v] + G[v][w]
            if w in D:
                if vwLength < D[w]:
                    raise ValueError("Dijkstra: found better path to already-final vertex")
            elif w not in Q or vwLength < Q[w]:
                Q[w] = vwLength
                P[w] = v

    return D

graph = {}
edge = []
def graph_maker(no_of_node, edge_list):
    global graph
    graph = {}

    for k in range(1, no_of_node+1):
        graph[k] = {}
    for u, v, w in edge_list:
        if v in graph[u]:
            if graph[v][u] > w:
                graph[u][v] = w
                graph[v][u] = w  #make graph undircted
        else:
            graph[u][v] = w
            graph[v][u] = w

    print(graph)








def shortestPath(graph,start,N):

    temp = Dijkstra(graph,start)
    for i in range(1, N+1):
        if str(i) == start:
            continue
        if str(i) not in temp:
            print(-1, end= " ")
        else:
            print(temp[str(i)], end=" ")
    print()


#graph_maker(5,edge)
#shortestPath(graph,'1',5)
if __name__ == '__main__':
    for _ in range(int(input())):
        edge = []
        N, M = map(int, input().split())
        for i in range(M):
            edge.append(tuple(map(int,input().strip().split())))
        start = int(input().strip())
        graph_maker(N,edge)
        shortestPath(graph, start, N)


'''
2
4 4
1 2 24
1 4 20
3 1 3
4 3 12
1
500 4
1 2 24
1 4 20
3 1 3
4 3 12
23 '''