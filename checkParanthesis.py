def checkParanthesis(string: str):
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}
    for i in string:
        if i in "({[":
            stack.append(i)
        elif i in ")}]":
            if not stack or stack[-1] != pairs[i]:
                return False
        return len(stack) == 0


a = checkParanthesis("([)]")
print(a)
