from collections import deque
def topoSort(adj_list):
    ans=[]
    queue = deque()
    indegrees = [0 for _ in range(len(adj_list))]
    for u,v in adj_list:
        adj_list[u].append(v)
        indegrees[v]+=1
    for i in range(0,len(indegrees)):
        if indegrees[i]==0:
            queue.append(i)
    while queue:
        node = queue.popleft()
        ans.append(node)
        for neighbour in adj_list[node]:
            if indegrees[neighbour]-1==0:
                queue.append(neighbour)
            indegrees[neighbour]-=1
    return ans

adjacency_list = [
    [0,1],
    [0,2],
    [1,2],
    [2,0]
]
ans = topoSort(adjacency_list)
print(ans)