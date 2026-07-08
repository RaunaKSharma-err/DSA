def sumAndMultiply(s,queries):
    ans=[]
    for u,v in queries:
        place = 1
        total = 0
        val = 0
        num = int(str(s)[u:v+1])
        while num:
            digit = num % 10
            if digit:
                total += digit
                val += digit * place
                place *= 10
            num //= 10
        ans.append(total * val)
    return ans

ans = sumAndMultiply(10203004,[[0,7],[1,3],[4,6]])
print(ans)