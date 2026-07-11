from collections import deque
def shortestPath(src, adjList):
    distance = [-1]*len(adjList)
    distance[src] = 0
    queue = deque([(src,0)])
    while queue:
        node,dist = queue.popleft()
        for neighbor in adjList[node]:
            if distance[neighbor]==-1:
                distance[neighbor] = dist+1
                queue.append((neighbor,dist+1))
    return distance

adjList= [
    [1,2],
    [0,2,4],
    [0,1,3],
    [2,5],
    [1,6],
    [3,6],
    [4,5,7,8],
    [6,8],
    [6,7]
]
ans = shortestPath(0,adjList)
print(ans)