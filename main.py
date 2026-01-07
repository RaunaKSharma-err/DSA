class solution:
    def threeSum(self, nums):
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                totalSum = nums[i] + nums[j] + nums[k]
                if totalSum < 0:
                    j += 1
                elif totalSum > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
        return result


m = [0, 0, 0, 0]
c = solution()
x = c.threeSum(m)
print(x)
