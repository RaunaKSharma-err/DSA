class solution:
    def fourSum(self, nums, target):
        n = len(nums)
        nums.sort()
        result = []
        for i in range(0, n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k = j + 1
                l = n - 1
                while k < l:
                    totalsum = nums[i] + nums[j] + nums[k] + nums[l]
                    if totalsum == target:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while l > k and nums[l] == nums[l + 1]:
                            l -= 1
                    elif totalsum < target:
                        k += 1
                    else:
                        l -= 1
        return result


m = [1, 0, -1, 0, -2, 2]
c = solution()
x = c.threeSum(m, 0)
print(x)
