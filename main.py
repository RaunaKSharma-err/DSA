class solution:
    def threeSum(self, nums, target):
        result = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for l in range(k + 1, len(nums)):
                        if (
                            nums[i] + nums[j] + nums[k] + nums[l] == target
                            and i != j
                            and i != k
                            and i != l
                            and j != k
                            and j != l
                            and k != l
                        ):
                            temp = [nums[i], nums[j], nums[k], nums[l]]
                            temp.sort()
                            if temp not in result:
                                result.append(temp)
        return result


m = [2, 2, 2, 2, 2]
c = solution()
x = c.threeSum(m, 8)
print(x)
