import heapq,sys
def minimumEffortPath(grid):
    row = len(grid)
    col = len(grid[0])
    effortArray = [[sys.maxsize] *col for _ in range(row)]
    PriorityQueue = [[0,0,0]]
    effortArray[0][0] = 0
    while PriorityQueue:
        r,c,effort = heapq.heappop(PriorityQueue)
        if r == row-1 and c == col-1:
            return effort
        for dx,dy in [(-1,0),(0,-1),(1,0),(0,1)]:
            new_r,new_c = r+dx,c+dy
            if new_r < 0 or new_r >= row or new_c < 0 or new_c >= col:
                continue
            newEffort = max(effort,abs(grid[new_r][new_c] - grid[r][c]))
            if newEffort < effortArray[new_r][new_c]:
                effortArray[new_r][new_c] = newEffort
                heapq.heappush(PriorityQueue, (new_r, new_c, newEffort))
    return effort

ans = minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]])
print(ans)