# Minimum Bit Flips to Convert Number.
start = 10
goal = 7
n = start ^ goal
count = 0
for i in range(0, 32):
    if n & (1 << i) != 0:
        count += 1
print(count)


# Single Number | Bit Manipulation
nums = [5, 5, 2, 1, 2, 2, 3, 1, 3]
ans = 0
for i in nums:
    ans = ans ^ i
print(ans)

# subsets

n = [1, 2, 3, 4]
length = len(n)
subsets = 1 << length
res = []

for nums in range(0, subsets):
    lst = []
    for i in range(0, length):
        if nums & (1 << i) != 0:
            lst.append(n[i])
    res.append(lst)
print(res)

# Generate Subsequences with Sum K

nums = [5, 9, 3, 4, 1]
taget = 9


def generateSubsequence(nums, target):
    res = []
    n = len(nums)
    subsets = 1 << n
    for i in range(subsets):
        lst = []
        for j in range(n):
            if i & (1 << j) != 0:
                lst.append(nums[j])
        if sum(lst) == target:
            res.append(lst)
    return res


print(generateSubsequence(nums, taget))


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
