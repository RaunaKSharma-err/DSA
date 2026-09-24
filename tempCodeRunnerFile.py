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