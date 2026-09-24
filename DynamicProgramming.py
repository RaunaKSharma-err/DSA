# climbing stairs leetcode problem

# ----recursive solution -----
def climbingStairs(index):
    if index ==1 or index ==0:
        return 1
    return climbingStairs(index-1)+climbingStairs(index-2)

# ----memoization solution ----
dp = [-1]*(5+1)
def climbingStairs(index,dp):
    if index ==1 or index ==0:
        return 1
    if dp[index]!=-1:
        return dp[index]
    dp[index] = climbingStairs(index-1,dp)+climbingStairs(index-2,dp)
    return dp[index]

# ----tablulation solution ----
def climbingStairs(index,dp):
    dp[0]=1
    dp[1]=1
    for i in range(2,index+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[index]

# ----tabulation solution ----
def climbingStairs(index):
    if index <=2:
        return index
    prev=1
    prev1=1
    for _ in range(2,index+1):
        prev,prev1 = prev1,prev+prev1
    return prev1
ans = climbingStairs(5)
print(ans)

def robHouse(index):
    prev=nums[0]
    prev1 = 0
    for i in range(1,index):
        if i >1:
            pick = nums[i]+prev1
        else:
            pick = nums[i]
        notpick = 0+prev
        prev,prev1 = max(pick,notpick),prev
    return prev

nums=[2,7,9,3,1]
ans = robHouse(len(nums))
print(ans)

def solve(index,maximum):
    if index >= len(nums[0]-1):
        return
    maximum = nums[0][index] + nums[1][index+1]

nums = [[20,60,2],[10,130,12]]
ans = solve(0)
print(ans)


# Unique paths leetcode solution

def uniquePaths(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    prev = [0]*n
    for i in range(m):
        curr=[0]*n
        for j in range(n):
            if i == 0 and j == 0 and obstacleGrid[i][j]!=1:
                curr[j] = 1
            else:
                up = prev[j] if i > 0 and obstacleGrid[i][j] != 1 else 0
                left = curr[j - 1] if j > 0 and obstacleGrid[i][j] != 1 else 0
                curr[j] = up + left
        prev = curr
    return prev[n-1]
ans = uniquePaths([[0,0,0],[0,1,0],[0,0,0]])
print(ans)

def minimumPathSum(m,n,grid):
    prev = [0]*n
    for i in range(m):
        curr = [0]*n
        for j in range(n):
            if i ==0 and j==0:
                curr[0] = grid[0][0]
                continue
            if i==0:
                up = float("inf")
            else:
                up = prev[j]
            if j==0:
                left = float("inf")
            else:
                left = curr[j-1]
            curr[j] = grid[i][j]+min(up,left)
        prev = curr.copy()
        return prev[n-1]

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

# tabulation with space optimization

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

def minFallingPathSum(grid):
    # RECURSION
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
    
    # MEMOIZATION
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
    ans = float("inf")
    for j in range(r):
        ans = min(ans , Memoization(0,j))
    # return ans
    
    #TABULATION
    def tabulation():
        for j in range(r):
            dp[r-1][j] = grid[r-1][j]
        for i in range(r-2,-1,-1):
            for j in range(r):
                down = dp[i+1][j]
                leftDiagonal = dp[i+1][j-1] if j > 0 else float("inf")
                rightDiagonal = dp[i+1][j+1] if j < r-1 else float("inf")
                dp[i][j] = grid[i][j] + min(down, leftDiagonal, rightDiagonal)
        return min(dp[0])

    #TABULATION WITH SPACE OPTIMIZATION
    def SOtabulation():
        prev = grid[r-1]
        for i in range(r-2,-1,-1):
            curr = [-1]*r
            for j in range(r):
                down = prev[j]
                leftDiagonal = prev[j-1] if j > 0 else float("inf")
                rightDiagonal = prev[j+1] if j < r-1 else float("inf")
                curr[j] = grid[i][j] + min(down, leftDiagonal, rightDiagonal)
            prev = curr
        return min(prev)
    return SOtabulation()
 
ans = minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])
print(ans)

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
        return maxi

    def Memoization(i, j1, j2):
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
                    ans = current + Memoization(
                        i + 1,
                        j1 + new_j1,
                        j2 + new_j2
                    )
                    maxi = max(maxi, ans)
            dp[i][j1][j2] = maxi
            return dp[i][j1][j2]

    def Tabulation():
        pass
    
    return Memoization(0, 0, c - 1)

ans = cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]])
print(ans)


def reverseDegreeOfString(val):
    total =0
    for i, ch in enumerate(val, 1):
        total += (123 - ord(ch)) * i
    return total
ans = reverseDegreeOfString("abc")
print(ans)

def PartitionEqualSubsetSum(nums , target):
    def Recursion(index,total):
        if index >= len(nums):  
            return target == total            
        pick = Recursion(index + 1, total+ nums[index])
        notPick = Recursion(index + 1, total)
        return pick or notPick

    dp = [[False for _ in range(len(nums))]for _ in range(target)]
    def Memoization(index,total):
        if total == 0:
            return True
        if index == 0:
            if nums[0] == total:
                return True
        if dp[index][total] != False:
            return True
        if nums[index] > total:
            pick = False
        else:
            pick = Memoization(index + 1, total+ nums[index])
        notPick = Memoization(index + 1, total)
        dp[index][total] =  pick or notPick
        return dp[index][total]

    def Tabulation():
        pass
    return Memoization(0,0)

nums = [1,5,11,5]
target = sum(nums)//2
print(PartitionEqualSubsetSum(nums,target))

from collections import deque
def minOperation(nums,x):
    count =0
    num = deque(nums)
    while x!=0:
        if x >= num[0] >= num[-1]:
            x -=num[0]
            num.popleft()
        else:
            x-= num[-1]
            num.pop()
        count+=1
    return count
ans = minOperation([1,1,4,2,3],5)
print(ans)

