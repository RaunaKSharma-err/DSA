def islands(grid):
    def dfs(grid, visited, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return
        if visited[r][c] ==1:
            return
        if grid[r][c]=="0":
            return
        visited[r][c] = 1
        dfs(grid, visited, r - 1, c)
        dfs(grid, visited, r, c-1)
        dfs(grid, visited, r, c +1)
        dfs(grid, visited, r+1, c)
    count=0
    rows = len(grid)
    cols = len(grid[0])
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=="1" and visited[r][c]==0:
                count+=1
                dfs(grid,visited,r,c)
    return count

ans = islands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])
print(ans)