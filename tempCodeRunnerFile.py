def islands(grid):
    def dfs(r,c,base_r,base_c,shape,visited,rows,cols,grid):
        visited[r][c] = 1
        shape.append((r-base_r,c-base_c))
        for x,y in [(-1,0),(0,-1),(1,0),(0,1)]:
            new_i,new_j = r+x,y+c
            if r < 0 or r >= rows or c < 0 or c >= cols:
                continue
            if visited[r][c] ==1:
                continue
            if grid[r][c]=="0":
                continue
            dfs(new_i,new_j,base_r,base_c,shape,visited,rows,cols,grid)
    uniqueIsland = set()
    rows = len(grid)
    cols = len(grid[0])
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=="1" and visited[r][c]==0:
                shape=[]
                dfs(r,c,r,c,shape,visited,rows,cols,grid)
                uniqueIsland.add(tuple(shape))
    return len(uniqueIsland)

ans = islands([
  ["0","1","1","0","1","1"],
  ["0","0","1","0","0","0"],
  ["1","1","0","1","1","0"],
  ["0","0","0","0","1","0"]
])
print(ans)