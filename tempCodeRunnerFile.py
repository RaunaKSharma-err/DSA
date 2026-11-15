def generate(numRows):
    if numRows == 1:
        return [[1]]
    res = [[1],[1,1]]
    if numRows == 2:
        return res
    prev = [1,1]
    for i in range(2,numRows):
        curr= [1 for _ in range(i+1)]
        for j in range(1,i):
            curr[j] = prev[j-1]+prev[j]
        prev = curr
        res.append(prev)
    return res

print(generate(5))