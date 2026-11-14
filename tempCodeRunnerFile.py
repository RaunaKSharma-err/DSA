def minimumSumSubarray(nums,l,r):
    if l > len(nums) > r:
        return 0
    window_sum1 = sum(nums[:l])
    window_sum2 = sum(nums[:r])
    min_sum1 = window_sum1
    min_sum2 = window_sum2
    for right in range(l, len(nums)):
        window_sum1 += nums[right] - nums[right-l]
        min_sum1 = min(abs(min_sum1), abs(window_sum1))
    for right in range(r, len(nums)):
        window_sum2 += nums[right] - nums[right-r]
        min_sum2 = min(abs(min_sum2), abs(window_sum2))
    print(min_sum1,min_sum2)
    return max(min_sum1,min_sum2)

print(minimumSumSubarray([-2, 2, -3, 1],2,3))