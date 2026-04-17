def generateValidParenthesis(index, total):
    if index >= len(subset):
        if total == 0:
            result.append("".join(subset))
        return
    if total < 0 or total > len(subset) // 2:
        return

    subset[index] = "("
    sums = total + 1
    generateValidParenthesis(index + 1, sums)
    sums = total - 1
    subset[index] = ")"
    generateValidParenthesis(index + 1, sums)


subset = [""] * (2 * 3)
result = []
generateValidParenthesis(0, 0)
print(result)