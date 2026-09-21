def reverseDegreeOfString(val):
    total =0
    for ch in range(len(val)):
        total+= abs(ord(val[ch])-123) * (ch+1)
    return total
ans = reverseDegreeOfString("abc")
print(ans)