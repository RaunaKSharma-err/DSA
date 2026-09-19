def minimumPathSumInTriangular(grid):
    r = len(grid)
    dp = [[-1] * r for _ in range(r + 1)]

    def solve(i, j):
        if i == r:
            return grid[i][j]
        
        if dp[i][j] != -1:
            return dp[i][j]

        down = grid[i][j] + solve(i + 1, j)
        diagonal = grid[i][j] + solve(i + 1, j + 1)
        dp[i][j] = min(down, diagonal)
        return dp[i][j]

    def tabulation():
        prev = grid[r-1]
        for i in range(r-2,-1,-1):
            curr = [-1]*r
            for j in range(0,i+1):
                down = grid[i][j] + prev[j]
                diagonal = grid[i][j] + prev[j + 1]
                curr[j] = min(down, diagonal)
            prev = curr
        return prev[0]
    
    return tabulation()

ans = minimumPathSumInTriangular([[2],[3,4],[6,5,7],[4,1,8,3]])
print(ans)