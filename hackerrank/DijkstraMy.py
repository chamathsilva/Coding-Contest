__author__ = 'chamathsilva'
import heapq
graph = {}

class Node(object):
    def __init__(self):
        self.parent = None
        self.distance = -1
        self.visited = False
        self.adj = {}

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


def Dijkstra(graph, start):
    graph[start].distance = 0
    Q = [graph[start]]
    while Q:
        min_node = heapq.heappop(Q)
        if not min_node.visited:
            for v in min_node.adj:
                node = graph[v]
                if node.distance == -1:
                    node.distance = min_node.adj[v] + min_node.distance
                else:
                    node.distance = min(node.distance, min_node.adj[v] + min_node.distance)
                heapq.heappush(Q, node)
            min_node.visited = True


if __name__ == '__main__':

    T = int(input().strip())
    for _ in range(T):
        out = ""
        N, M = (int(x) for x in input().strip().split(' '))
        graph_maker(N, M)
        start = input().strip()
        Dijkstra(graph, start)
        for i in range(1, N+1):
            if i == int(start):
                continue
            out += str(graph[str(i)].distance) + str(" ")
            #print(graph[str(i)].distance, end=" ")
        print(out)
        #print("")







