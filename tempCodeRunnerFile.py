
def dfs(n, adjacency_list, node):
    visited = [False] * (n + 1)
    ans = []

    def dfs(node):
        visited[node] = True
        ans.append(node)
        for neighbor in adjacency_list[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    dfs(node)
    return ans


n = 8
adjacency_list = [[], [2, 4], [1, 3, 6], [2], [1, 5, 7], [4, 8], [2], [4, 8], [5, 7]]
ans = dfs(n, adjacency_list, 1)
print(ans)