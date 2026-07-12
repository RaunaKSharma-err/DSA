import heapq
def dijkstra(edges, src):
    adjList = [[] for _ in range(len(edges))]
    for u,v,w in edges:
        adjList[u].append([v,w])
    distance = ["inf"]*len(edges)
    queue = [[src,0]]
    while queue:
        node,dist = heapq.heappop(queue)
        if distance[node]!="inf":
            continue
        distance[node] = dist
        for neighbor,weight in adjList[node]:
            if distance[neighbor]=="inf":
                heapq.heappush(queue,(neighbor,dist+weight))
    return distance

edges= [
    [0,1,4],
    [0,2,4],
    [1,0,4],
    [1,2,2],
    [2,0,4],
    [2,1,2],
    [2,3,3],
    [2,4,1],
    [2,5,6],
    [3,2,3],
    [3,5,2],
    [4,2,1],
    [4,5,3],
    [5,2,6],
    [5,3,2],
    [5,4,3]
]
ans = dijkstra(edges,0)
print(ans)