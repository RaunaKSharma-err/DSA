from collections import deque
def safeNode(adjacency_list):
    ans=[]
    queue = deque()
    adj_list = [[]for _ in range(len(adjacency_list))]
    indegrees = [0 for _ in range(len(adj_list))]

    for node in range(len(adjacency_list)):
        for neighbor in adjacency_list[node]:
            adj_list[neighbor].append(node)
            indegrees[node]+=1
            
    for node in range(0,len(indegrees)):
        if indegrees[node]==0:
            queue.append(node)

    while queue:
        node = queue.popleft()
        ans.append(node)
        for neighbour in adj_list[node]:
            indegrees[neighbour] -= 1
            if indegrees[neighbour] == 0:
                queue.append(neighbour)
    return ans
adjacency_list = [
    [1,2],
    [2,3],
    [5],
    [0],
    [5],
    [],
    [],
]
ans = safeNode(adjacency_list)
print(ans)