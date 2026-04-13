subset = ["0"] * 3
result = []


def generateAllBinaryString(index, flag, subset, result):
    if index >= len(subset):
        result.append("".join(subset))
        return
    subset[index] = "0"
    generateAllBinaryString(index + 1, True, subset, result)
    if flag == True:
        subset[index] = "1"
        generateAllBinaryString(index + 1, False, subset, result)
        subset[index] = "0"


generateAllBinaryString(0, True, subset, result)
print(result)