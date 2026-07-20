
# shortest path using dijkstra algorithm
import heapq , sys
def shortesPath(edges, src, dest):
    adjList = [[] for _ in range(len(edges)//2)]
    path = []
    for u,v,w in edges:
        adjList[u].append([v,w])
    distance = [sys.maxsize] * len(adjList)
    parent = [-1] * len(adjList)
    priorityQueue = [[src,0]]
    parent[src] = [0]
    while priorityQueue:
        node,dist = heapq.heappop(priorityQueue)
        for neighbor,weight in adjList[node]:
            totalDist = dist+weight
            if totalDist < distance[neighbor]:
                distance[neighbor] = totalDist
                heapq.heappush(priorityQueue,(neighbor,totalDist))
                parent[neighbor] = node
    while dest != src:
        path.append(dest)
        dest = parent[dest]
    path.append(src)
    return path[::-1]


edges= [
    [1,2,2],
    [1,4,1],
    [2,1,2],
    [2,3,4],
    [2,5,5],
    [3,2,4],
    [3,4,3],
    [3,5,1],
    [4,1,1],
    [4,3,3],
    [5,2,5],
    [5,3,1],
]
ans = shortesPath(edges,1,5)
print(ans)