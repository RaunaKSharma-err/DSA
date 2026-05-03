
def rotatedString(s, goal):
    return len(s) == len(goal) and goal in s + s


s = "abcde"
goal = "deabc"
ans = rotatedString(s, goal)
print(ans)