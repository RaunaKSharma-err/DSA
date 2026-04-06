
# generate all subsequence using recursion
def solveSubSequence(index, subset, total):
    if target == total:
        result.append(subset.copy())
        return
    elif target < total:
        return
    if index >= len(nums):
        return

    subset.append(nums[index])
    sum = total + nums[index]
    solveSubSequence(index + 1, subset, sum)
    e = subset.pop()
    sum -= e
    solveSubSequence(index + 1, subset, sum)


nums = [5, 9, 3, 4, 1]
subset = []
result = []
target = 9
total = 0
solveSubSequence(0, subset, total)
print(result)