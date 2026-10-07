def longestSubArray(s1,s2):
    def Recursion(i,j,res):
        if i < 0 or j < 0:
            return res
        if s1[i]==s2[j]:
            return Recursion(i-1,j-1,s1[i]+res)
        return max(Recursion(i-1,j,""),Recursion(i,j-1,""),key=len)
    return Recursion(len(s1)-1,len(s2)-1,"")

print(longestSubArray("abxyzcd","123xyz456"))