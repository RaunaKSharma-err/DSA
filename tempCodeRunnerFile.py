def solve(subseq,index):
    if index >= len(lst):
        result.append(subseq.copy())
        return
    subseq.append(lst[index])
    solve(subseq,index+1)
    subseq.pop()
    solve(subseq,index+1)
    return

result=[]
lst = [1,5,8,9]
solve([],0)
print(result)