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