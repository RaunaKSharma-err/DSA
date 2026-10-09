def longestSubArray(s1,s2):
    # def Recursion(i, j):
    #     if i < 0 or j < 0:
    #         return 0
    
    #     if s1[i] == s2[j]:
    #         return 1+Recursion(i - 1, j - 1)
    #     return 0

    # dp=[[0 for _ in range(len(s2))] for _ in range(len(s1))]
    # def Memoization(i, j):
    #     if i < 0 or j < 0:
    #         return 0

    #     if dp[i][j] != 0:
    #         return dp[i][j]

    #     if s1[i] == s2[j]:
    #         dp[i][j] =Memoization(i - 1, j - 1) + 1
    #     return dp[i][j]
    
    # for i in range(len(s1)):
    #     for j in range(len(s2)):
    #         res = Memoization(i, j)
    #         if len(res) > len(best_str):
    #             best_str = res

    def Tabulation(s1,s2):
        m = len(s1)
        n = len(s2)
        maxi = float("-inf")
        dp=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                if s1[i] == s2[j]:
                    dp[i][j] =dp[i-1][j-1]+1
                maxi = max(maxi,dp[i][j])
        return maxi

    def spaceOptimization(s1,s2):
            m = len(s1)
            n = len(s2)
            maxi = float("-inf")
            prev = [0 for _ in range(n)]
            for i in range(1,m):
                curr = [0 for _ in range(n)]
                for j in range(1,n):
                    if s1[i] == s2[j]:
                        curr[j] =prev[j-1]+1
                    maxi = max(maxi,curr[j])
                prev = curr
            return maxi
        
    return spaceOptimization(s1,s2)


print(longestSubArray("abxyzcd","123xyz456"))