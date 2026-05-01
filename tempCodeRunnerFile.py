def rotateFunction(nums):
    greatest = 0
    for i in range(len(nums)):
        res = 0
        k = 0
        for j in range(-i, len(nums) - i):
            res += k * nums[j]
            k += 1
        greatest = res if greatest < res else greatest
    return greatest


nums = [100]
ans = rotateFunction(nums)
print(ans)