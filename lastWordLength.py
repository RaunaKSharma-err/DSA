def lastWordLength(str):
    count = 0
    for i in range(len(str) - 1, -1, -1):
        if str[i] == " " and count < 1:
            continue
        elif str[i] != " ":
            count += 1
        else:
            return count
    return count


str = " a"
a = lastWordLength(str)
print(a)
