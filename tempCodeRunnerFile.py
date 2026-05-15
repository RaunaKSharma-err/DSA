def nextGreaterElement(nums):
    stack = []
    n = len(nums)
    for i in range(2*n - 1, -1, -1):
        while len(stack) > 0 and nums[i%n] > stack[-1]:
            stack.pop()
        if i <n:
            if len(stack) != 0:
                ans[i]=stack[-1]
        stack.append(nums[i%n])


nums = [19, 2, 4, 9, 3, 5, 8, 10]
ans = [-1] * len(nums)
nextGreaterElement(nums)
print(ans)