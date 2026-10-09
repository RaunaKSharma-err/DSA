def longestSubArray(s1,s2):
    best = ""
    def Recursion(i,j,res):
        nonlocal best
        if i < 0 or j < 0:
            if len(res) > len(best):
                best = res
            return
        
        if s1[i]==s2[j]:
            Recursion(i-1,j-1,s1[i]+res)

        if len(res) > len(best):
            best = res

        Recursion(i - 1, j, "")
        Recursion(i, j - 1, "")
    Recursion(len(s1)-1,len(s2)-1,"")
    return best

print(longestSubArray("abxyzcd","123xyz456"))