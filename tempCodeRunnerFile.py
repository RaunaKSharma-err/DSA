def detectCycleInDG(adj_list):
    visited = [0 for _ in range(len(adj_list))]
    pathVisited = [0 for _ in range(len(adj_list))]

    def dfs(currNode,visited,pathVisited,adj_list):
        visited[currNode]=1
        pathVisited[currNode]=1
        for neighbour in adj_list[currNode]:
            if visited[neighbour]==0:
                x=dfs(neighbour,visited,pathVisited,adj_list)
                if x==True:
                    return True
            elif pathVisited[neighbour]==1:
                return True
        pathVisited[currNode]=0
        return False

    for i in range(0,len(adj_list)):
        if visited[i]==0:
            y = dfs(i,visited,pathVisited,adj_list)
            if y == True:
                return True
    return False

adjacency_list = [
    [],
    [2],
    [3,8],
    [4,7],
    [6],
    [4],
    [],
    [5],
    [9,10],
    [10]
]
ans = detectCycleInDG(adjacency_list)
print(ans)