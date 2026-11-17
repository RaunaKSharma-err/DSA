def getRow(rowIndex):
    res = []
    for i in range(rowIndex+1):
        curr = [1] * (i + 1)
        for j in range(1, i):
            curr[j] = res[i-1][j-1] + res[i-1][j]
        res.append(curr)
    return res[rowIndex]
print(getRow(3))