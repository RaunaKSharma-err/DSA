def findContentChildren(g, s):
    g.sort()
    s.sort()
    count = 0
    left = 0
    right = 0
    while left < len(g) and right < len(s):
        if g[left] <= s[right]:
            count += 1
            left += 1
            right += 1
        else:
            right += 1
    return count


g = [2, 6, 8, 1, 4]
s = [4, 2, 7, 1, 2, 3]
ans = findContentChildren(g, s)
print(ans)