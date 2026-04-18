
def combinationSum(index, total, subset):
    if total == 0:
        result.append(subset.copy())
        return

    if total < 0:
        return

    for i in range(index, len(nums)):
        if i > index and nums[i] == nums[i - 1]:
            continue

        subset.append(nums[i])
        combinationSum(i + 1, total - nums[i], subset)
        subset.pop()


target = 4
result = []
subset = []
nums = [1, 1, 1, 2, 3]

combinationSum(0, target, subset)
print(result)