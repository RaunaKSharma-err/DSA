def smallestIndex(nums):
    sum=0
    for n in nums:
        if nums[n]==n:
            return n
        else:
            for i in str(n):
                sum += int(i)
            if sum == n:
                return n
ans = smallestIndex([1,10,11])
print(ans)