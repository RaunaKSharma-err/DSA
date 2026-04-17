
def combinationSum(index, total, subset):
    if sum(subset) == target:
        result.append(subset.copy())
        return
    if index >= len(nums):
        return
    if total > target:
        return
    subset.append(nums[index])
    sums = total + nums[index]
    combinationSum(index, sums, subset)
    subset.pop()
    sums = total
    combinationSum(index + 1, sums, subset)


target = 7
result = []
subset = []
nums = [2, 3, 6, 7]
combinationSum(0, 0, subset)
print(result)
