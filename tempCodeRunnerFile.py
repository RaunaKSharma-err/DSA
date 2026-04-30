# rat in the maze

nums = [[0] * 4 for _ in range(4)]
nums[0][0] = 1
nums[1][0] = 1
nums[1][1] = 1
nums[2][0] = 1
nums[2][1] = 1
nums[3][1] = 1
nums[3][2] = 1
nums[3][3] = 1
n = len(nums)
visited = [[0] * 4 for _ in range(4)]
result = []


def ratMaze(row, col, res):
    if row == n - 1 and col == n - 1:
        result.append("".join(res))
        return
    visited[row][col] = 1

    # downward
    if row + 1 < n and nums[row + 1][col] == 1 and not visited[row + 1][col]:
        res.append("D->")
        ratMaze(row + 1, col, res)
        res.pop()

    # left
    if col - 1 >= 0 and nums[row][col - 1] == 1 and not visited[row][col - 1]:
        res.append("L->")
        ratMaze(row, col - 1, res)
        res.pop()

    # right
    if col + 1 < len(visited) and nums[row][col + 1] == 1 and not visited[row][col + 1]:
        res.append("R->")
        ratMaze(row, col + 1, res)
        res.pop()

    # up
    if row - 1 >= 0 and nums[row - 1][col] == 1 and not visited[row - 1][col]:
        res.append("U->")
        ratMaze(row - 1, col, res)
        res.pop()

    visited[row][col] = 0


ratMaze(0, 0, [])
print(result)