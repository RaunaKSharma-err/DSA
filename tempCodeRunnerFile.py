def minFallingPathSum(grid):
    # recursion
    r = len(grid)
    def Recursion(i, j):
        if j < 0 or j >= r:
            return float("inf")
        if i == r-1 :
            return grid[i][j]
        down = grid[i][j] + Recursion(i + 1, j)
        leftDiagonal = grid[i][j] + Recursion(i + 1, j + 1)
        rightDiagonal = grid[i][j] + Recursion(i + 1, j - 1)
        return min(down, leftDiagonal, rightDiagonal)
    
    #memoization
    dp = [[-1]*r for _ in range(r)]
    def Memoization(i,j):
        if j < 0 or j >= r:
            return float("inf")
        if i == r-1 :
            return grid[i][j]
        if dp[i][j] != -1:
            dp[i][j] = grid[i][j]
        down = grid[i][j] + Memoization(i + 1, j)
        leftDiagonal = grid[i][j] + Memoization(i + 1, j + 1)
        rightDiagonal = grid[i][j] + Memoization(i + 1, j - 1)
        dp[i][j] =  min(down, leftDiagonal, rightDiagonal)
        return dp[i][j]
    
    # ans = float("inf")
    # for j in range(r):
    #     ans = min(ans , Memoization(0,j))
    # return ans
    
    #tabulation
    def tabulation():
        for i in range(r):
            for j in range(r):
                if j < 0 or j >= r:
                    return float("inf")
                if i == r-1 :
                    return grid[i][j]
                if dp[i][j] != -1:
                    dp[i][j] = grid[i][j]
                down = grid[i][j] + dp[i + 1][j]
                leftDiagonal = grid[i][j] + dp[i + 1][j+1]
                rightDiagonal = grid[i][j] + dp[i + 1][j-1]
                dp[i][j] =  min(down, leftDiagonal, rightDiagonal)
        return dp[r-1][r-1]
    return tabulation()
 
ans = minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])
print(ans)