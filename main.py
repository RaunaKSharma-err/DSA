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

# generate the binary subsequence


def generateParanthesis(index, total):
    if index >= len(brackets):
        if total == 0:
            result.append("".join(brackets))
        return
    if total > len(brackets) // 2:
        return
    elif total < 0:
        return
    brackets[index] = "("
    sums = total + 1
    generateParanthesis(index + 1, brackets, sums)
    brackets[index] = ")"
    sums = total - 1
    generateParanthesis(index + 1, brackets, sums)


brackets = [""] * (2 * 4)
result = []
total = 0
generateParanthesis(0, total)
print(result)
