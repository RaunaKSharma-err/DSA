def longestCommonSubsequence(text1,text2):
    def Recursion(index1,index2):
        if index1 < 0 or index2 < 0:
            return 0            
        if text1[index1]==text2[index2]:
            return 1 + Recursion(index1-1,index2-1)
        return max(Recursion(index1-1,index2),Recursion(index1,index2-1))

    dp=[[-1 for _ in range(len(text2)+1)]for _ in range(len(text1)+1)]
    def Memoization(index1,index2):
        if index1 < 0 or index2 < 0:
            return 0      
        if dp[index1][index2]!=-1:
            return dp[index1][index2]    
        if text1[index1]==text2[index2]:
            dp[index1][index2]= 1 + Memoization(index1-1,index2-1)
            return dp[index1][index2]
        dp[index1][index2] = max(Memoization(index1-1,index2),Memoization(index1,index2-1))
        return dp[index1][index2]

    def Tabulation(m,n):
        for i in range(m):
            dp[i][0]=0
        for i in range(n):
            dp[0][i]=0
        for index1 in range(1,m+1):
            for index2 in range(1,n+1):
                if text1[index1-1]==text2[index2-1]:
                    dp[index1][index2]= 1 + dp[index1-1][index2-1]
                else:
                    dp[index1][index2] = max(dp[index1-1][index2],dp[index1][index2-1])
        return dp[m][n]

    def SpaceOptimization(text1,text2):
        m = len(text1)
        n = len(text2)
        prev = [-1 for _ in range(n+1)]
        for i in range(n):
            prev[i]=0
        for index1 in range(1,m+1):
            curr = [-1 for _ in range(n+1)]
            for index2 in range(1,n+1):
                if text1[index1-1]==text2[index2-1]:
                    curr[index2]= 1 + prev[index2-1]
                else:
                    curr[index2] = max(prev[index2],curr[index2-1])
            prev=curr
        return prev[n]
    return SpaceOptimization(text1,text2)
    
print(longestCommonSubsequence("ac","acexyzh"))