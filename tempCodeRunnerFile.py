def sumAndMultiply(nums):
    total = 0
    val = 0
    place = 1
    while nums:
        digit = nums % 10
        if digit:
            total += digit
            val += digit * place
            place *= 10
        nums //= 10
    return total * val

ans = sumAndMultiply(10203004)
print(ans)