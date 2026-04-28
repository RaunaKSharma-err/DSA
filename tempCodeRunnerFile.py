def reverseInteger(n):
    temp = f"{n:b}"
    rev = ""
    for i in temp:
        rev = i + rev
    return int(rev, 2)


c = reverseInteger(25)
print(c)
