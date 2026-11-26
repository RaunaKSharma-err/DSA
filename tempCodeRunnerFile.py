def stoneRemovalGame(n):
    if n < 10:
        return False
    for i in range(10,3,-1):
        if n < i:
            if i % 2 == 0:
                return False
            else:
                return True
        n-=i

print(stoneRemovalGame(1))