__author__ = 'chamathsilva'

graph = {}
edge = []
def graph_maker(no_of_node, edge_list):
    global graph
    for k in range(1, no_of_node+1):
        graph[str(k)] = []
    for u, v in edge_list:
        graph[u].append(v)


def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        #print(queue)
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)


for z in range (int(input())):
    graph = {}
    edge = []
    N, M = map(int, input().split())
    for _ in range(M):
        edge.append(tuple(input().split()))
    start = input()

    graph_maker(N,edge)

    for i in range(1,N+1):
        if str(i) == start:
            continue
        else:
            temp = bfs(graph,start,str(i))

            if temp is None:
                print(-1,end = " ")
            else:
                print((len(temp)-1) * 6, end=" ")
    print()
