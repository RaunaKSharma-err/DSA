def solve(val,index):
    if index >= len(lst) or len(val)>3:
        return
    if len(val) == 3 and int(val)%2==0:
        result.append(int(val.copy()))
        return
    val += str(lst[index])
    solve(val,index+1)
    val = val[:-1]
    solve(val,index+1)

lst = [2,1,3,0]
result = []
solve("",0)
print(result)