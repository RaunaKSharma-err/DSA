from collections import deque
def decodeString(s):
    stack = deque([])
    prevString = ""
    repeatCount=0
    for ch in s:
        if ch.isdigit():
            repeatCount = repeatCount*10+int(ch)
        elif ch =="[":
            stack.append((repeatCount,prevString))
            prevString=""
            repeatCount=0
        elif ch=="]":
            m,n = stack.pop()
            prevString = n+prevString*m
        else:
            prevString += ch
    return prevString

print(decodeString("3[a]2[bc]"))