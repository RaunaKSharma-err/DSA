from collections import deque
def nearestZero(mat):
    row = len(mat)
    col = len(mat[0])
    visited = [[0  for _ in range(col)] for _ in range(row)]
    distance = [[0  for _ in range(col)] for _ in range(row)]
    queue = deque()
    for i in range(row):
        for j in range(col):
            if mat[i][j] == 0:
                queue.append([i,j,0])
                visited[i][j] = 1
    while queue:
        i,j,d = queue.popleft()
        distance[i][j] = d
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            new_x, new_y = i + dx, j + dy
            if 0 <= new_x < row and 0 <= new_y < col and not visited[new_x][new_y]:
                visited[new_x][new_y] = 1
                queue.append([new_x, new_y, d + 1])
    return distance

matrix = [[0, 1, 0], [0, 0, 1], [0, 1, 1]]
ans = nearestZero(matrix)
print(ans)