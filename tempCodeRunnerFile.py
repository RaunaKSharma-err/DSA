# generate all subsequence using recursion
def solveSubSequence(index, total):
    if target == total:
        return 1
    elif target < total:
        return 0
    if index >= len(nums):
        return 0
    sum = total + nums[index]
    pick = solveSubSequence(index + 1, sum)
    sum = total
    notPick = solveSubSequence(index + 1, sum)
    return pick + notPick


nums = [5, 9, 3, 4, 1]
target = 9
total = 0
result = solveSubSequence(0, total)
print(result)