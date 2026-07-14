def sequentialDigits(low, high):
    ans = []
    for start in range(1, 10):
        num = start
        for nxt in range(start + 1, 10):
            num = num * 10 + nxt
            if low <= num <= high:
                ans.append(num)
    return ans
ans = sequentialDigits(1000,13000)
print(ans)