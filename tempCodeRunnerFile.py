
from functools import lru_cache
def isMatch(s,p):
    # @lru_cache(None)
    def match(i, j):
        if i < 0 and j < 0:
            return True
        if j < 0:
            return False
        if p[j] == "*":
            zero = match(i, j-2)
            if i >= 0 and (p[j-1] == "." or s[i] == p[j-1]):
                multiple = match(i-1, j)
                return zero or multiple
            return zero
        if i >= 0 and (p[j] == "." or s[i] == p[j]):
            return match(i-1, j-1)
        return False
    return match(len(s)-1, len(p)-1)


print(isMatch("abbb","ab*"))