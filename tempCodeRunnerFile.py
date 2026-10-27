def isAnagram(s,t):
    if len(s) != len(t):
        return False
    look = {}
    for i in s:
        look[i] = look.get(i,0)+1
    for i in t:
        if i not in look or look[i]==0:
            return False
        look[i]-=1
    return True
print(isAnagram("rat", "car"))