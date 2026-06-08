from collections import deque
def numEnclaves(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    queue = deque()
    for r in range(rows):
        for c in range(cols):
            if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and grid[r][c] == 1:
                queue.append((r,c))
                visited[r][c]=1
    while len(queue)!=0:
        r,c = queue.popleft()
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            new_x, new_y = r + dx, c + dy
            if new_x <0 or new_x<0 or new_x>=rows or new_y>=cols:
                continue
            if grid[new_x][new_y]==0:
                continue
            if grid[new_x][new_y]==1 and visited[new_x][new_y]==1:
                continue
            queue.append((new_x,new_y))
            visited[new_x][new_y]=1
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]==1 and  visited[i][j]==0:
                count+=1
    return count


ans = numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])
print(ans)