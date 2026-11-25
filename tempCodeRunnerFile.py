def smallestUniqueSubarray(nums):
    hashMap = {nums[0]:1}
    for i in range(1,len(nums)):
        hashMap[nums[i]] = hashMap.get(nums[i],0)+1
        hashMap[(nums[i-1],nums[i])] = hashMap.get((nums[i-1],nums[i]),0)+1
    mini=float("inf")
    for i in hashMap:
        if mini > hashMap[i]:
            mini = hashMap[i]
            ans = i
    return ans if isinstance(ans,int) else len(ans)

print(smallestUniqueSubarray([1,1,2,2,1]))