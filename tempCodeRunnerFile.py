def isBipartite(adjlist):
    visited=[-1 for _ in range(len(adjlist))]
    def dfs(node,color):
        visited[node]=color
        for neighbour in adjlist[node]:
            if visited[neighbour]==-1:
                if dfs(neighbour,1-color):
                    return True
            elif visited[neighbour]==color:
                return False 
        return True
    for node in range(len(adjlist)):
        if visited[node] == -1:
            if not dfs(node, 0):
                return False
    return True

adjacency_list = [[1,3],[0,2],[1,3],[0,2]]
ans = isBipartite(adjacency_list)
print(ans)