def solve(res,total,index):
    if index >= 6:
        if total == 0:
            result.append("".join(res))
        return
    if total < 0 or total >3:
        return
    res[index]="("
    solve(res,total+1,index+1)
    res[index]=")"
    solve(res,total-1,index+1)

result=[]
brackets=[""]*6
solve(brackets,0,0)
print(result)