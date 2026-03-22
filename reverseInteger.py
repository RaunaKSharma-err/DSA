def reverseInteger(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    val = 0
    while n != 0:
        temp = n % 10
        val = val * 10 + temp
        n = n // 10
    val *= sign
    if val < -2147483648 or val > 2147483647:
        return 0
    return val


print(reverseInteger(2147483647))
