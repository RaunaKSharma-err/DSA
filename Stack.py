class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def pushs(self, val):
        self.items.append(val)

    def pops(self):
        if len(self.items) == 0:
            return "stack is empty"
        x = self.items.pop()
        return x

    def top(self):
        if len(self.items) == 0:
            return "no top, stack is empty"
        x = self.items[-1]
        return x

    def size(self):
        return len(self.items)


s = Stack()
s.pushs(1)
s.pushs(2)
s.pushs(3)
s.pushs(4)
s.pops()
s.top()

# stack implementation using queue

from collections import deque
from itertools import count


class stack:
    def __init__(self):
        self.items = deque([])

    def push(self, val):
        self.items.append(val)
        for _ in range(len(self.items) - 1):
            self.items.append(self.items.popleft())

    def pop(self):
        if len(self.items) == 0:
            return "stack is empty"
        return self.items.popleft()

    def top(self):
        if len(self.items) == 0:
            return "stack is empty"
        return self.items[0]


lst = stack()
lst.push(100)
lst.push(200)
lst.push(300)
print(lst)
lst.pop()
print(lst)
lst.top()


# implement queue using stack

from collections import deque


class queue:
    def __init__(self):
        self.st1 = deque([])
        self.st2 = deque([])

    def push(self, val):
        if len(self.st1) != 0:
            for _ in range(len(stack)):
                self.st2.append(self.st1.pop())
        self.st1.append(val)
        for _ in range(len(self.st2)):
            self.st1.append(self.st1.pop())

    def pop(self):
        if len(self.st1) == 0:
            return "queue is empty"
        return self.st1.popleft()

    def top(self):
        if len(self.st1) == 0:
            return "queue"
        return self.st1[0]


lst = queue()
lst.push(100)
lst.push(200)
lst.push(300)
print(lst)
lst.pop()
print(lst)
lst.top()

# getmin in o(1) leetcode problem
from collections import deque


class stack:
    def __init__(self):
        self.items = deque([])

    def push(self, val):
        self.items.append(val)
        mini = min(self.items, self.pop, val)
        self.items.append(mini)

    def pop(self):
        if len(self.items) == 0:
            return "stack is empty"
        return self.items.popleft()

    def top(self):
        if len(self.items) == 0:
            return "stack is empty"
        return self.items[0]

    def getminimum(self):
        return self.items[len(self.items) - 1]


lst = stack()
lst.push(100)
lst.push(200)
lst.push(300)
print(lst)
lst.pop()
print(lst)
lst.top()


# next greatear element solution


def nextGreaterElement(nums):
    stack = []
    n = len(nums)
    for i in range(n - 1, 0, -1):
        while len(stack) > 0 and nums[i] > stack[-1]:
            stack.pop()
        if len(stack) != 0:
            ans[i] = stack[-1]
        stack.append(nums[i])


nums = [19, 2, 4, 9, 3, 5, 8, 10]
ans = [-1] * len(nums)
nextGreaterElement(nums)
print(ans)

# next greatear element|| solution


def nextGreaterElement(nums):
    stack = []
    n = len(nums)
    for i in range(2 * n - 1, -1, -1):
        while len(stack) > 0 and nums[i % n] > stack[-1]:
            stack.pop()
        if i < n:
            if len(stack) != 0:
                ans[i] = stack[-1]
        stack.append(nums[i % n])


nums = [19, 2, 4, 9, 3, 5, 8, 10]
ans = [-1] * len(nums)
nextGreaterElement(nums)
print(ans)

# asteroid collision leetcode solution


def asteroidCollision(nums):
    stack = []
    for i in nums:
        while stack and i < 0 < stack[-1]:
            if stack[-1] < -i:
                stack.pop()
                continue
            if stack[-1] == -i:
                stack.pop()
            break
        else:
            stack.append(i)
    return stack


nums = [4, 7, 1, 1, 2, -3, -7, 17, 15, -16]
ans = asteroidCollision(nums)
print(ans)

# longest substring without repeating characters


def lengthOfLongestSubstring(s):
    left = 0
    maxi = 0
    hashmap = dict()
    for right in range(len(s)):
        if s[right] in hashmap and hashmap[s[right]] >= left:
            left = hashmap[s[right]] + 1

        hashmap[s[right]] = right
        maxi = max(maxi, right - left + 1)
    return maxi


s = "abcabcbb"
ans = lengthOfLongestSubstring(s)
print(ans)

# max consecutive ones leetcode solution


def maxConsecutiveOnes(nums, k):
    left = 0
    right = 0
    maxi = 0
    zero = 0
    n = len
    while right < len(nums):
        if nums[right] == 0:
            zero += 1
        if zero > k:
            if nums[left] == 0:
                zero -= 1
            left += 1
        if zero <= k:
            maxi = max(maxi, right - left + 1)
        right += 1
    return maxi


ans = maxConsecutiveOnes([1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
print(ans)


# fruits in the basket leetcode solution


def totalFruit(nums):
    right = 0
    left = 0
    maxi = 0
    mydict = {}
    while right < len(nums):
        mydict[nums[right]] = mydict.get(nums[right], 0) + 1
        if len(mydict) > 2:
            mydict[nums[left]] -= 1
            if mydict[nums[left]] == 0:
                del mydict[nums[left]]
            left += 1
        if len(mydict) <= 2:
            maxi = max(maxi, right - left + 1)
        right += 1
    return maxi


ans = totalFruit([3, 3, 3, 1, 2, 1, 3, 2, 1, 2, 4])
print(ans)


# 1432. maximum points you can obtain from cards leetcode solution


def maxScore(cardPoints, k):
    n = len(cardPoints)
    leftsum = 0
    rightsum = 0
    for i in range(k):
        leftsum += cardPoints[i]
    maxi = leftsum
    rightidx = n - 1
    for i in range(k - 2, -1, -1):
        leftsum -= cardPoints[i]
        rightsum -= cardPoints[n - k + i]
        maxi = max(maxi, leftsum + rightsum)
        rightidx -= 1
    return maxi


cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3
ans = maxScore(cardPoints, k)
print(ans)

# assign cookies leetcode solution


def findContentChildren(g, s):
    g.sort()
    s.sort()
    count = 0
    left = 0
    right = 0
    while left < len(g) and right < len(s):
        if g[left] <= s[right]:
            count += 1
            left += 1
        right += 1
    return count


g = [2, 6, 8, 1, 4]
s = [4, 2, 7, 1, 2, 3]
ans = findContentChildren(g, s)
print(ans)


# Minimum number of coins leetcode solution


def coinChange(coins, amount):
    coinSet = []
    coins.sort(reverse=True)
    for coin in coins:
        while amount >= coin:
            amount -= coin
            coinSet.append(coin)

    if amount == 0:
        return coinSet
    return []


coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
amount = 43
ans = coinChange(coins, amount)
print(ans)


# lemonade change leetcode solution


def lemonadeChange(bills):
    n = len(bills)
    five = 0
    ten = 0
    for i in range(n):
        if bills[i] == 5:
            five += 1
        elif bills[i] == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        else:
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True


bills = [5, 5, 10, 10, 20]
ans = lemonadeChange(bills)
print(ans)


# jump game leetcode solution
def canJump(nums):
    n = len(nums)
    maxReach = 0
    for i in range(n):
        if i > maxReach:
            return False
        maxReach = max(maxReach, i + nums[i])
    return True


nums = [3, 2, 1, 0, 0, 2, 1, 5]
ans = canJump(nums)
print(ans)


# jump game II leetcode solution
def canjump(nums):
    jump = 0
    left = 0
    right = 0
    n = len(nums)
    while right <= n - 1:
        farthest = 0
        for i in range(left, right + 1):
            farthest = max(farthest, i + nums[i])
        left = right + 1
        right = farthest
        jump += 1
    return jump


nums = [2, 3, 4, 4, 1, 1, 1, 2]
ans = canjump(nums)
print(ans)