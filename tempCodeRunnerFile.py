
def lengthOfLongestSubstring(s):
    left = 0
    maxi = 0
    hashmap = dict()
    for right in range(len(s)):
        if s[right] in hashmap and hashmap[s[right]] >= left:
            left = hashmap[s[right]] + 1

        hashmap[s[right]] = right
        maxi = max(maxi, right - left + 1)
    return maxi


s = "abcabcbb"
ans = lengthOfLongestSubstring(s)
print(ans)
