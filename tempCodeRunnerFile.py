def solve(subseq,index,total):
    if index >= len(lst):
        if target == total:
            result.append(subseq.copy())
            return  True
        return
    subseq.append(lst[index])
    total += lst[index]
    if solve(subseq,index+1,total):
        return True
    val = subseq.pop()
    total -= val
    if solve(subseq,index+1,total):
        return True
    return  False

lst = [5,9,3,4,1]
target=4
result=[]
ans = solve([],0,0)
print(ans,result)