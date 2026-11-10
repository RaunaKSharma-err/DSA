def climbStairs(n,costs):
    def Recurrsion(i):
        if i == n:
            return 0
        min1 = float("inf")
        min2 = float("inf")
        min3 = float("inf")
        if i+1 <= n:
            min1 = costs[i] + 1**2 + Recurrsion(i+1)
        if i+2 <= n:
            min2 = costs[i+1] + 2**2 + Recurrsion(i+2)
        if i+3 <= n:
            min3 = costs[i+2] + 3**2 + Recurrsion(i+3)
        return min(min1, min2, min3)

    dp = [-1 for _ in range(n)]
    def Memoization(i):
        if i == n:
            return 0
        if dp[i] != -1:
            return dp[i]
        min1 = float("inf")
        min2 = float("inf")
        min3 = float("inf")
        if i+1 <= n:
            min1 = costs[i] + 1**2 + Recurrsion(i+1)
        if i+2 <= n:
            min2 = costs[i+1] + 2**2 + Recurrsion(i+2)
        if i+3 <= n:
            min3 = costs[i+2] + 3**2 + Recurrsion(i+3)
        dp[i] =  min(min1, min2, min3)
        return dp[i]

    def Tabulation():
        dp = [0 for _ in range(n+1)]
        dp[n]=0
        for i in range(n-1,-1,-1):
            min1 = float("inf")
            min2 = float("inf")
            min3 = float("inf")
            if i+1 <= n:
                min1 = costs[i] + 1**2 + dp[i+1]
            if i+2 <= n:
                min2 = costs[i+1] + 2**2 + dp[i+2]
            if i+3 <= n:
                min3 = costs[i+2] + 3**2 + dp[i+3]
            dp[i] =  min(min1, min2, min3)
        return dp[0]

    def SpaceOptimization():
        next1 = 0
        next2 = 0
        next3 = 0
        for i in range(n-1, -1, -1):
            min1 = costs[i] + 1 + next1
            min2 = float("inf")
            min3 = float("inf")
            if i+2 <= n:
                min2 = costs[i+1] + 4 + next2
            if i+3 <= n:
                min3 = costs[i+2] + 9 + next3
            curr = min(min1, min2, min3)
            next3 = next2
            next2 = next1
            next1 = curr
        return next1
    return SpaceOptimization()
print(climbStairs(4,[1,2,3,4]))