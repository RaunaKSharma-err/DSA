def minimizeSum(nums):
    # mini = float("+inf")
    # maxi = float("-inf")
    # for i in range(len(nums)-1):
    #     if nums[i] == nums[i-1]:
    #         continue
    #     for j in range(i+1,len(nums)):
    #         mini = min(mini,abs(nums[i]-nums[j]))
    #         maxi = max(maxi,abs(nums[i]-nums[j]))

    nums = sorted(nums)
    return nums[len(nums)-1]-nums[2]

print(minimizeSum([9,2, 3]))