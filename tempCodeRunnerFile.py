def climbingStairs(index):
    prev=1
    prev1=1
    for _ in range(2,index+1):
        curr = prev+prev1
        prev = prev1
        prev1=curr
    return prev1

ans = climbingStairs(5)
print(ans)