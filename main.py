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

# combination sums problem |||


def combinationSum3(last, total, subset):
    if total == n and len(subset) == k:
        result.append(subset.copy())
        return
    if total > n or len(subset) > k:
        return
    for i in range(last, 10):
        sum = total + i
        subset.append(i)
        combinationSum3(i + 1, sum, subset)
        subset.pop()


target = 4
result = []
subset = []
nums = [1, 1, 1, 2, 3]

combinationSum3(0, target, subset)
print(result)

# generate the combination of the letter from the numbers


def findLetterCombination(index, subset):
    if index >= len(digit):
        result.append("".join(subset))
        return
    for ch in use_map[digit[index]]:
        subset.append(ch)
        findLetterCombination(index + 1, subset)
        subset.pop()


use_map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
digit = "46"
result = []
subset = []
findLetterCombination(0, [])
print(result)


# subset sum


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

# N - Queens leetcode problem
n = 4
ans = []
board = ["." * n for _ in range(n)]
leftRow = [0] * n
upperDiagonal = [0] * (2 * n - 1)
lowerDiagonal = [0] * (2 * n - 1)


def findNQueen(col, n, board, ans, leftRow, upperDiagonal, lowerDiagonal):
    if col == n:
        ans.append(board[:])
        return
    for row in range(n):
        if (
            leftRow[row] == 0
            and lowerDiagonal[row + col] == 0
            and upperDiagonal[n - 1 + col - row] == 0
        ):
            board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
            leftRow[row] = 1
            lowerDiagonal[row + col] = 1
            upperDiagonal[n - 1 + col - row] = 1
            findNQueen(col + 1, n, board, ans, leftRow, upperDiagonal, lowerDiagonal)
            board[row] = board[row][:col] + "." + board[row][col + 1 :]
            leftRow[row] = 0
            lowerDiagonal[row + col] = 0
            upperDiagonal[n - 1 + col - row] = 0


findNQueen(0, n, board, ans, leftRow, upperDiagonal, lowerDiagonal)
print(ans)

# Furthest Point From Origin


def moveFurthestPointFromOrigin(moves):
    left = right = blank = 0
    for i in moves:
        if i == "L":
            left += 1
        elif i == "R":
            right += 1
        else:
            blank += 1
    return abs(left - right) + blank


moves = "_R__LL_"
res = moveFurthestPointFromOrigin(moves)
print(res)

# climbing stair problem


def findTheSteps(index, total, subset, count):
    if index >= n:
        if total == 0:
            count += 1
        return
    if total < 0:
        return
    subset.append(1)
    sums = total - subset[index]
    findTheSteps(index + 1, sums, subset, count)
    subset[index] = 2
    sums = total - subset[index]
    findTheSteps(index + 1, sums, subset, count)


n = 5
count = 0
findTheSteps(0, 5, [], 0)
print(count)


# reverse bit leetcode solution
def reverseBit(n):
    res = 0
    for _ in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res


reverseBit(25)

# rat in the maze

nums = [[0] * 4 for _ in range(4)]
nums[0][0] = 1
nums[1][0] = 1
nums[1][1] = 1
nums[2][0] = 1
nums[2][1] = 1
nums[3][1] = 1
nums[3][2] = 1
nums[3][3] = 1
n = len(nums)
visited = [[0] * 4 for _ in range(4)]
result = []


def ratMaze(row, col, res):
    if row == n - 1 and col == n - 1:
        result.append("".join(res))
        return
    visited[row][col] = 1

    # downward
    if row + 1 < n and nums[row + 1][col] == 1 and not visited[row + 1][col]:
        res.append("D->")
        ratMaze(row + 1, col, res)
        res.pop()

    # left
    if col - 1 >= 0 and nums[row][col - 1] == 1 and not visited[row][col - 1]:
        res.append("L->")
        ratMaze(row, col - 1, res)
        res.pop()

    # right
    if col + 1 < len(visited) and nums[row][col + 1] == 1 and not visited[row][col + 1]:
        res.append("R->")
        ratMaze(row, col + 1, res)
        res.pop()

    # up
    if row - 1 >= 0 and nums[row - 1][col] == 1 and not visited[row - 1][col]:
        res.append("U->")
        ratMaze(row - 1, col, res)
        res.pop()

    visited[row][col] = 0


ratMaze(0, 0, [])
print(result)


# rotate function leetcode solution
# brute force solution
def rotateFunction(nums):
    greatest = 0
    for i in range(len(nums)):
        res = 0
        k = 0
        for j in range(-i, len(nums) - i):
            res += k * nums[j]
            k += 1
        greatest = res if greatest < res else greatest
    return greatest


nums = [100]
ans = rotateFunction(nums)
print(ans)

# optimal solution


def rotateFunction(nums):
    n = len(nums)
    total_sum = sum(nums)

    F = sum(i * num for i, num in enumerate(nums))
    max_val = F

    for k in range(1, n):
        F = F + total_sum - n * nums[-k]
        max_val = max(max_val, F)

    return max_val


# longest substring problem


def longestSubstring(s):
    last_seen = {}
    left = 0
    result = 0

    for right, ch in enumerate(s):
        if ch in last_seen:
            left = max(left, last_seen[ch] + 1)
        last_seen[ch] = right
        result = max(result, right - left + 1)
    return result


s = "tmmzuxt"
a = longestSubstring(s)
print(a)

# rotate the string leetcode problem


def rotatedString(s, goal):
    return len(s) == len(goal) and goal in s + s


s = "abcde"
goal = "deabc"
ans = rotatedString(s, goal)
print(ans)


# largest palindrome leetcode problem


def largestPlaindrome(s):
    # Transform string
    t = "#" + "#".join(s) + "#"
    n = len(t)
    p = [0] * n

    center = 0
    right = 0
    max_len = 0
    max_center = 0

    for i in range(n):
        mirror = 2 * center - i

        if i < right:
            p[i] = min(right - i, p[mirror])

        # Expand around center i
        while (
            i - p[i] - 1 >= 0
            and i + p[i] + 1 < n
            and t[i - p[i] - 1] == t[i + p[i] + 1]
        ):
            p[i] += 1

        # Update center and right boundary
        if i + p[i] > right:
            center = i
            right = i + p[i]

        # Track max palindrome
        if p[i] > max_len:
            max_len = p[i]
            max_center = i

    start = (max_center - max_len) // 2
    return s[start : start + max_len]


s = "cbbd"
res = largestPlaindrome(s)
print(res)


# minimum platforms leetcode problem
def minimumPlatform(arr, dep):
    arr.sort()
    dep.sort()
    platform_needed = 1
    max_platforms = 1
    j = 0
    i = 1
    while i < len(arr) and j < len(dep):
        if arr[i] <= dep[j]:
            platform_needed += 1
            i += 1
        else:
            platform_needed -= 1
            j += 1
        max_platforms = max(max_platforms, platform_needed)
    return max_platforms


ans = minimumPlatform(
    [900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]
)
print(ans)

# MaximumPathSum leetcode problem


def MaximumPathSum(root):
    maxi = 0

    def solve(node):
        if node is None:
            return 0
        leftSum = solve(node.left)
        if leftSum < 0:
            leftSum = 0
        rightSum = solve(node.right)
        if rightSum < 0:
            rightSum = 0
        maxi = max(maxi, leftSum + rightSum + node.val)
        return max(leftSum, rightSum) + node.val

    solve(root)
    return maxi


# top view of the binary tree


class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = node(3)
root.left = node(2)
root.right = node(9)
root.right.left = node(8)
root.right.right = node(5)
root.left.left = node(4)
root.left.right = node(6)
root.left.left.right = node(1)


# def topView(node):
#     if node is None:
#         return None
#     queue = [(node, 0)]
#     top_view = {}
#     while queue:
#         current_node, line = queue.pop(0)
#         if line not in top_view:
#             top_view[line] = current_node.val
#         if current_node.left:
#             queue.append((current_node.left, line - 1))
#         if current_node.right:
#             queue.append((current_node.right, line + 1))
#     return [top_view[key] for key in sorted(top_view.keys())]


# ans = topView(root)
# print(ans)


# def bottomView(node):
#     if node is None:
#         return None
#     queue = [(node, 0)]
#     bottom_view = {}
#     while queue:
#         current_node, line = queue.pop(0)
#         bottom_view[line] = current_node.val
#         if current_node.left:
#             queue.append((current_node.left, line - 1))
#         if current_node.right:
#             queue.append((current_node.right, line + 1))
#     return [bottom_view[key] for key in sorted(bottom_view.keys())]


# ans = bottomView(root)
# print(ans)


def RightView(root):
    def solve(node, level, ans):
        if node is None:
            return
        if len(ans) == level:
            ans.append(node.val)
        if node.right:
            solve(node.right, level + 1, ans)
        if node.left:
            solve(node.left, level + 1, ans)
    ans=[]
    solve(root, 0, ans)
    return ans

ans = RightView(root)
print(ans)


def missingMultiple(nums, k):
    hs =set(nums)
    for num in range(k,101,k):
        if num not in hs:
            return num

ans = missingMultiple([8,2,3,4,6],2)
print(ans)

def solve(subseq,index,total):
    if index >= len(lst):
        if target == total:
            result.append(subseq.copy())
        return
    subseq.append(lst[index])
    total += lst[index]
    solve(subseq,index+1,total)
    val = subseq.pop()
    total -= val
    solve(subseq,index+1,total)
    return

lst = [5,9,3,4,1]
result = []
target=9
solve([],0,0)
print(result)

def solve(subseq,index,total):
    if index >= len(lst):
        if target == total:
            result.append(subseq.copy())
            return  True
        return
    subseq.append(lst[index])
    total += lst[index]
    if solve(subseq,index+1,total):
        return True
    val = subseq.pop()
    total -= val
    if solve(subseq,index+1,total):
        return True
    return  False

lst = [5,9,3,4,1]
target=4
result=[]
ans = solve([],0,0)
print(ans,result)

def backtrack(flag,nums,index):
    if index >= len(nums):
        result.append("".join(nums))
        return
    nums[index] = "0"
    backtrack(True,nums,index+1)
    if flag == True:
        nums[index]= "1"
        backtrack(False,nums,index+1)
        nums[index]="0"

nums=[0]*3
result=[]
backtrack(True,nums,0)

print(result)

def myPow(x,n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / myPow(x, -n)
    half = myPow(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x

ans = myPow(2.00000,10)
print(ans)

def solve(res,total,index):
    if index >= 6:
        if total == 0:
            result.append("".join(res))
        return
    if total < 0 or total >3:
        return
    res[index]="("
    solve(res,total+1,index+1)
    res[index]=")"
    solve(res,total-1,index+1)

result=[]
brackets=[""]*6
solve(brackets,0,0)
print(result)

def backtrack(res,index,sum):
    if index >=len(nums) or sum < 0:
        return
    if sum == 0:
        result.append(res.copy())
        return
    res.append(nums[index])
    sum -= nums[index]
    backtrack(res,index,sum)
    sum += nums[index]
    res.pop()
    backtrack(res,index+1,sum) 

nums = [2,3,6,7]
target=7
result=[]
backtrack([],0,7)
print(result)

def isPowerOfThree(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 3 != 0:
        return False
    return isPowerOfThree(n // 3)

ans = isPowerOfThree(27)
print(ans)

def fib(n):
    if n==1:
        return 1
    if n==0:
        return 0
    return fib(n-1)+fib(n-2)

ans = fib(8)
print(ans)

def solve(val,index):
    if index >= len(lst) or len(val)>3:
        return
    if len(val) == 3 and int(val)%2==0:
        result.append(int(val.copy()))
        return
    val += str(lst[index])
    solve(val,index+1)
    val = val[:-1]
    solve(val,index+1)

lst = [2,1,3,0]
result = []
solve("",0)
print(result)

def letterCombination(index,digits,subset):
    if index >= len(digits):
        result.append("".join(subset))
        return
    for ch in use_map[digits[index]]:
        subset.append(ch)
        letterCombination(index+1,digits,subset)
        subset.pop()

use_map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
result=[]
letterCombination(0,"46",[])
print(result)

def solve(n):
    result = [["."] * n for _ in range(n)]
    rows = set()
    diag1 = set()
    diag2 = set()
    def backtrack(col):
        if col == n:
            return True
        for row in range(n):
            if (
                row not in rows
                and row - col not in diag1
                and row + col not in diag2
            ):
                result[row][col] = "Q"
                rows.add(row)
                diag1.add(row - col)
                diag2.add(row + col)
                if backtrack(col + 1):
                    return True
                result[row][col] = "."
                rows.remove(row)
                diag1.remove(row - col)
                diag2.remove(row + col)
        return False
    backtrack(0)
    return ["".join(row) for row in result]
ans = solve(4)
print(ans)