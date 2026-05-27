# jump game leetcode solution
def canJump(nums):
    n = len(nums)
    maxReach = 0
    for i in range(n):
        if i > maxReach:
            return False
        maxReach = max(maxReach, i + nums[i])
    return True


nums = [3, 2, 1, 0, 0, 2, 1, 5]
ans = canJump(nums)
print(ans)