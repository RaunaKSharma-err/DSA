def solve(n):
    result = [["."]*n for _ in range(n)]
    def issafe(row,col):
        for dx,dy in [[-1,-1],[1,-1],[0,-1]]:
            r = row
            c = col
            while  0 <= r < n and 0 <= c < n :
                if result[r][c] == "Q":
                    return False
                r+=dx
                c+=dy
        return True
    def backtrack(col):
        if col == n:
            return True
        for row in range(n):
            if issafe(row, col):
                result[row][col] = "Q"
                if backtrack(col + 1):
                    return True
                result[row][col] = "."
        return False

    backtrack(0)
    return ["".join(result[i]) for i in range(n)]
ans = solve(4)
print(ans)