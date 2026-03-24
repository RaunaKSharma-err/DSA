s = "A man, a plan, a canal: Panama"


def validPalindrome(s):
    a = ""
    for i in s:
        if i == " " or i == "," or i == ":":
            continue
        a += i
    b = a[::-1]
    print(a, b)
    if a == b:
        return True
    return False


print(validPalindrome(s))