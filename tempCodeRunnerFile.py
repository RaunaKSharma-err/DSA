from collections import deque


def bfs(n, adjacency_list):
    queue = deque()
    visited = [False] * (n + 1)
    ans =[]
    for i in range(1, n + 1):
        for j in adjacency_list[i]:
            if not visited[j]:
                queue.append(j)
                visited[j] = True
                while queue:
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
ans = bfs(n, adjacency_list)
print(ans)