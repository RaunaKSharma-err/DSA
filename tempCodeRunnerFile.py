def maxConsecutiveOnes(nums, k):
    left = 0
    right = 0
    maxi = 0
    zero = 0
    n = len
    while right < len(nums):
        if nums[right] == 0:
            zero += 1
        if zero > k:
            if nums[left] == 0:
                zero -= 1
            left += 1
        if zero <= k:
            maxi = max(maxi, right - left + 1)
        right += 1
    return maxi


ans = maxConsecutiveOnes([1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
print(ans)