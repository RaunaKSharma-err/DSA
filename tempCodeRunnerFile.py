def longestSubstring(s):
    last_seen = {}
    left = 0
    result = 0

    for right, ch in enumerate(s):
        if ch in last_seen:
            left = max(left, last_seen[ch] + 1)
        last_seen[ch] = right
        result = max(result, right - left + 1)
    return result


s = "tmmzuxt"
a = longestSubstring(s)
print(a)