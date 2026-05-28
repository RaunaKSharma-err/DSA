def canjump(nums):
    jump = 0
    left = 0
    right = 0
    n = len(nums)
    while right <= n - 1:
        farthest = 0
        for i in range(left, right + 1):
            farthest = max(farthest, i + nums[i])
        left = right + 1
        right = farthest
        jump += 1
    return jump


nums = [2, 3, 4, 4, 1, 1, 1, 2]
ans = canjump(nums)
print(ans)