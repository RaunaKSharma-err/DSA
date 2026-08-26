def solve(subseq,index,total):
    if index >= len(lst):
        if target == total:
            result.append(subseq.copy())
        return
    subseq.append(lst[index])
    total += lst[index]
    solve(subseq,index+1,total)
    val = subseq.pop()
    total -= val
    solve(subseq,index+1,total)
    return

lst = [5,9,3,4,1]
result = []
target=9
solve([],0,0)
print(result)