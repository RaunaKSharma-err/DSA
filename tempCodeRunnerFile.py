
def findSubsetSum(index, total):
    if index >= len(nums):
        result.append(total)
        return
    sums = total + nums[index]
    findSubsetSum(index + 1, sums)
    findSubsetSum(index + 1, total)


result = []
nums = [5, 9, 3]
findSubsetSum(0, 0)
print(result)