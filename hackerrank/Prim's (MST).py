__author__ = 'chamathsilva'
import heapq
graph = {}

class Node(object):
    def __init__(self):
        self.parent = None
        self.distance = float('inf')
        self.visited = False
        self.adj = {}
        self.inheap = False

    def __repr__(self):
        return "color :" + " adj:" + str(self.adj) + "distance:" + str(self.distance) + "\n"

    def __lt__(self, other):
        return self.distance < other.distance

def graph_maker(no_of_node, no_of_edge):
    global graph
    graph = {}
    for k in range(1, no_of_node+1):
        graph[str(k)] = Node()
    for _ in range(no_of_edge):

        u, v, w = (input().split())
        if v not in graph[u].adj:
            graph[u].adj[v] = int(w)
            graph[v].adj[u] = int(w)
        else:
            if int(w) < graph[u].adj[v]:
                graph[u].adj[v] = int(w)
                graph[v].adj[u] = int(w)

def Prim(graph, start):
    graph[start].distance = 0
    Q = [graph[start]]
    while Q:
        min_node = heapq.heappop(Q)
        min_node.inheap = False
        if not min_node.visited:
            for v in min_node.adj:
                node = graph[v]
                if not node.visited and min_node.adj[v] < node.distance:
                    node.distance = min_node.adj[v]
                    node.parent = min_node
                #if node in Q:
                    #Q.remove(node)
                    #heapq.heapify(Q))
                if node.inheap:
                    Q.remove(node)
                    heapq.heapify(Q)

                heapq.heappush(Q, node)
                node.inheap = True

            min_node.visited = True



if __name__ == '__main__':
    N, M = (int(x) for x in input().strip().split(' '))
    graph_maker(N, M)
    start = input().strip()
    Prim(graph, start)
    #print(graph)
    print(sum([i.distance for i in graph.values()]))

