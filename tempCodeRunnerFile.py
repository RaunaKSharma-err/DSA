
def solveSubSequence(index, subset):
    if index >= len(nums):
        result.append(subset.copy())
        return
    subset.append(nums[index])
    solveSubSequence(index + 1, subset)
    subset.pop()
    solveSubSequence(index + 1, subset)


nums = [1, 2, 3, 4]
subset = []
result = []
solveSubSequence(0, subset)
print(result)
