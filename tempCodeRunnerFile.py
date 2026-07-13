import sys
def dijkstraSet(edges,src):
    adjList = [[] for _ in range(len(edges))]
    for u,v ,w in edges:
        adjList[u].append([v,w])
    distance = [sys.maxsize for _ in range(len(edges))]
    distance[src] = 0
    myset = set()
    myset.add((0,src))
    while len(myset) !=0:
        dist,node = min(myset)
        myset.discard((dist,node))
        for neighbor ,weight in adjList[node]:
            distanceTravel = dist+weight
            if distanceTravel < distance[neighbor]:
                if distance[neighbor]!=sys.maxsize:
                    myset.discard((distance[neighbor],neighbor))
                distance[neighbor] = distanceTravel
                myset.add((distanceTravel,neighbor))
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
ans = dijkstraSet(edges,0)
print(ans)