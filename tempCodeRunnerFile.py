# generate all subsequence using recursion
def solveSubSequence(index, subset, total):
    if target == total:
        result.append(subset.copy())
        return True
    elif target < total:
        return False
    if index >= len(nums):
        return False
    subset.append(nums[index])
    sum = total + nums[index]
    pick = solveSubSequence(index + 1, subset, sum)
    if pick == True:
        return True
    subset.pop()
    sum = total
    notPick = solveSubSequence(index + 1, subset, sum)
    return notPick


nums = [5, 9, 3, 4, 1]
subset = []
result = []
target = 9
total = 0
solveSubSequence(0, subset, total)
print(result)
