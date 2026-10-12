def solve(text1,text2):
    m = len(text1)
    n = len(text2)
    prev = [0 for _ in range(n+1)]
    for i in range(n):
        prev[i]=0
    for index1 in range(1,m+1):
        curr = [0 for _ in range(n+1)]
        for index2 in range(1,n+1):
            if text1[index1-1]==text2[index2-1]:
                curr[index2]= 1 + prev[index2-1]
            else:
                curr[index2] = max(prev[index2],curr[index2-1])
        prev=curr
    return m+n-(prev[n]*2)
print(solve("leetcode","etco"))