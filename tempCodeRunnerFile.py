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