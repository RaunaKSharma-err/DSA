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

# Rotting oranges leetcode problem


def orangesRotting(grid):
    rows = len(grid)
    cols = len(grid[0])
    queue = deque()
    fresh_oranges = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                fresh_oranges += 1

    minutes = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue and fresh_oranges > 0:
        minutes += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (
                    0 <= new_x < rows
                    and 0 <= new_y < cols
                    and grid[new_x][new_y] == 1
                ):
                    grid[new_x][new_y] = 2
                    fresh_oranges -= 1
                    queue.append((new_x, new_y))

    return minutes if fresh_oranges == 0 else -1

ans = orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
print(ans)
   
#flood fill leetcode problem
from collections import deque
from copy import deepcopy

def floodFill(image, sr, sc, newColor):
    rows = len(image)
    cols = len(image[0])
    visited = deepcopy(image)
    queue = deque()
    queue.append((sr, sc))
    if image[sr][sc] == newColor:
        return image
    while queue:
        x,y = queue.popleft()
        visited[x][y] = newColor
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and visited[new_x][new_y] == image[sr][sc]:
                queue.append((new_x, new_y))
    return visited


ans = floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
print(ans)

#detect cycle in undirected graph
from collections import deque
def has_cycle(v,e, adjacency_list):
    visited = [False] * (v + 1)
    queue = deque()
    for i in range(1,v+1):
        if visited[i]:
            continue
        queue.append((i, -1))
        visited[i] = True
        while queue:
            node, parent = queue.popleft()
            for neighbor in adjacency_list[node]:
                if not visited[neighbor]:
                    visited[neighbor]=True
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    return True
    return False   
        
adjacency_list = [
    [],
    [2,4],
    [1, 3, 6],
    [2],
    [1, 5],
    [4, 7],
    [2, 7],
    [5,6],
]
ans = has_cycle(7, 7,adjacency_list)
print(ans)

