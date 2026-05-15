def nextGreaterElement(nums):
    stack = []
    n = len(nums)
    for i in range(n - 1, 0, -1):
        while len(stack) > 0 and nums[i] > stack[-1]:
            stack.pop()
        if len(stack) != 0:
            ans[i]=stack[-1]
        stack.append(nums[i])


nums = [19, 2, 4, 9, 3, 5, 8, 10]
ans = [-1] * len(nums)
nextGreaterElement(nums)
print(ans)