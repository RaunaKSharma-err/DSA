def cherryPickup(grid):
    r = len(grid)
    c = len(grid[0])
    dp = [[[-1 for _ in range(c)]for _ in range(c)]for _ in range(r)]
    def Recursion(i, j1, j2):
        if j1 < 0 or j1 >= c or j2 < 0 or j2 >= c:
            return float("-inf")
        
        if i == r - 1:
            if j1 == j2:
                return grid[i][j1]
            return grid[i][j1] + grid[i][j2]
        
        if dp[i][j1][j2]!=-1:
            return dp[i][j1][j2]
        
        if j1 == j2:
            current = grid[i][j1]
        else:
            current = grid[i][j1] + grid[i][j2]

        maxi = float("-inf")

        for new_j1 in range(-1, 2):
            for new_j2 in range(-1, 2):
                ans = current + Recursion(
                    i + 1,
                    j1 + new_j1,
                    j2 + new_j2
                )
                maxi = max(maxi, ans)
        dp[i][j1][j2] = maxi
        return dp[i][j1][j2]
    return Recursion(0, 0, c - 1)

ans = cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]])
print(ans)