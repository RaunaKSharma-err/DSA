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