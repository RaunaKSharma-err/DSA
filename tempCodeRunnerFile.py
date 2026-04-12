def generateParanthesis(index, total, brackets):
    if index >= len(brackets):
        if total == 0:
            result.append("".join(brackets))
        return
    if total > len(brackets) // 2:
        return
    elif total < 0:
        return
    brackets[index] = "("
    sums = total + 1
    generateParanthesis(index + 1, sums)
    brackets[index] = ")"
    sums = total - 1
    generateParanthesis(index + 1, sums)


brackets = [""] * (2 * 4)
result = []
total = 0
generateParanthesis(0, total, brackets)
print(result)