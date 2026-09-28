def evaluate(str,knowledge):
    val=""
    temp=""
    flag=False
    for i in range(len(str)-1,-1,-1):
        if str[i]==")":
            flag=True
            continue
        if str[i]=="(":
            for arr in knowledge:
                if arr[0] == temp:
                    val = arr[1]+val
            flag=False
            temp=""
            continue
        if flag:
            temp=str[i]+temp
            continue
        val =str[i]+val
    return val
ans = evaluate("(name)is(age)yearsold",[["name","bob"],["age","two"]])
print(ans)