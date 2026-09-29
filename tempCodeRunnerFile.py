def maximumParanthesisDepth(s):
    count=maxi=0
    for ch in s:
        if ch=="(":
            count+=1
        if ch==")":
            count-=1
        maxi = max(maxi,count)
    return maxi
print(maximumParanthesisDepth("(1+(2*3)+((8)/4))+1"))