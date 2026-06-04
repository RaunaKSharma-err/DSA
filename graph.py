from collections import deque


def bfs(n, adjacency_list, starting_node):
    ans = []
    queue = deque()
    visited = [False] * (n + 1)
    queue.append(starting_node)
    visited[starting_node] = True

    while len(queue) != 0:
        node = queue.popleft()
        ans.append(node)
        for neighbor in adjacency_list[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    return ans


n = 9
adjacency_list = [
    [],
    [2, 8],
    [1, 3, 4],
    [2],
    [2, 5],
    [4, 6],
    [5, 7],
    [6, 8],
    [1, 7, 9],
    [8],
]
ans = bfs(n, adjacency_list, 2)
print(ans)

# DFS


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

