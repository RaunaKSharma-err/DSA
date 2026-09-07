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