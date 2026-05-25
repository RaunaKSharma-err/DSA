def lemonadeChange(bills):
    mydict = {5: 0, 10: 0, 20: 0}
    for bill in bills:
        if bill == 5:
            mydict[5] += 1
        elif bill == 10:
            mydict[10] += 1
            if mydict[5] > 0:
                mydict[5] -= 1
            else:
                return False
        if bill == 20:
            mydict[20] += 1
            if mydict[10] > 0 and mydict[5] > 0:
                mydict[10] -= 1
                mydict[5] -= 1
            else:
                return False
    return True


bills = [5, 5, 10, 10, 20]
ans = lemonadeChange(bills)
print(ans)