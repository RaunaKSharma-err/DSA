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