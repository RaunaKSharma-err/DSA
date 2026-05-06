def largestPlaindrome(s):
    result = ""
    for i in range(len(s)):
        temp = ""
        original = ""
        for j in range(i, len(s)):
            original += s[j]
            temp = s[j] + temp
            if temp == original and len(temp) > len(result):
                result = temp
    return result


s = "cbbd"
res = largestPlaindrome(s)
print(res)