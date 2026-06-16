def processString(val):
    res=""
    for i in val:
        if i == "#":
            res +=res
        elif i == "%":
            res = res[::-1]
        elif i == "*":
            res = res[:len(res)-1]
        else:
            res += i
    return res
ans = processString("z*#")
print(ans)