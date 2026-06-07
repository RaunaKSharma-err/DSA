def surroundedRegions(board):
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    def dfs(i,j):
        visited[i][j] = True
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            new_x, new_y = i + dx, j + dy
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and not visited[new_x][new_y] and board[new_x][new_y] == "O":
                dfs(new_x, new_y)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "O" and not visited[i][j]:
                dfs(i, j)
    return board

ans = surroundedRegions([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]])
print(ans)