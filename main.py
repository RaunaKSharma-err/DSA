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

# generate all the binary string
subset = ["0"] * 3
result = []


def generateAllBinaryString(index, flag, subset, result):
    if index >= len(subset):
        result.append("".join(subset))
        return
    subset[index] = "0"
    generateAllBinaryString(index + 1, True, subset, result)
    if flag == True:
        subset[index] = "1"
        generateAllBinaryString(index + 1, False, subset, result)
        subset[index] = "0"


generateAllBinaryString(0, True, subset, result)
print(result)


def solveSubSequence(index, total, subset):
    if total == 0:
        result.append(subset.copy())
        return
    elif total < 0:
        return
    if index >= len(nums):
        return
    for i in range(index, n):
        if i > index and nums[i] == nums[i - 1]:
            continue
    subset.append(nums[index])
    sums = total - nums[index]
    solveSubSequence(i + 1, sums, subset)
    subset.pop()


# check for a valid palindrome
def checkValidPalindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


res = checkValidPalindrome("A man, a plan, a canal: Panama")
print(res)


# generate valid paranthesis


def generateValidParenthesis(index, total):
    if index >= len(subset):
        if total == 0:
            result.append("".join(subset))
        return
    if total < 0 or total > len(subset) // 2:
        return

    subset[index] = "("
    sums = total + 1
    generateValidParenthesis(index + 1, sums)
    sums = total - 1
    subset[index] = ")"
    generateValidParenthesis(index + 1, sums)


subset = [""] * (2 * 3)
result = []
generateValidParenthesis(0, 0)
print(result)

# combination sums problem


def combinationSum1(index, total, subset):
    if sum(subset) == target:
        result.append(subset.copy())
        return
    if index >= len(nums):
        return
    if total > target:
        return
    subset.append(nums[index])
    sums = total + nums[index]
    combinationSum1(index, sums, subset)
    subset.pop()
    sums = total
    combinationSum1(index + 1, sums, subset)


target = 7
result = []
subset = []
nums = [2, 3, 6, 7]
combinationSum1(0, 0, subset)
print(result)

# combination sums problem ||


def combinationSum2(index, total, subset):
    if total == 0:
        result.append(subset.copy())
        return
    if total < 0:
        return
    for i in range(index, len(nums)):
        if i > index and nums[i] == nums[i - 1]:
            continue
        subset.append(nums[i])
        combinationSum2(i + 1, total - nums[i], subset)
        subset.pop()


target = 4
result = []
subset = []
nums = [1, 1, 1, 2, 3]

combinationSum2(0, target, subset)
print(result)
