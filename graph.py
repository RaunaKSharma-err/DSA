from collections import deque

def bfs(n, adjacency_list, starting_node):
    ans = []
    queue = deque()
    visited = [False] * (n + 1)
    queue.append(starting_node)
    visited[starting_node] = True

    while len(queue) != 0:
        node = queue.popleft()
        ans.append(node)
        for neighbor in adjacency_list[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    return ans


n = 9
adjacency_list = [
    [],
    [2, 8],
    [1, 3, 4],
    [2],
    [2, 5],
    [4, 6],
    [5, 7],
    [6, 8],
    [1, 7, 9],
    [8],
]
ans = bfs(n, adjacency_list, 2)
print(ans)

# DFS


def dfs(n, adjacency_list, node):
    visited = [False] * (n + 1)
    ans = []

    def dfs(node):
        visited[node] = True
        ans.append(node)
        for neighbor in adjacency_list[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    dfs(node)
    return ans


n = 8
adjacency_list = [[], [2, 4], [1, 3, 6], [2], [1, 5, 7], [4, 8], [2], [4, 8], [5, 7]]
ans = dfs(n, adjacency_list, 1)
print(ans)

# Rotting oranges leetcode problem


def orangesRotting(grid):
    rows = len(grid)
    cols = len(grid[0])
    queue = deque()
    fresh_oranges = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                fresh_oranges += 1

    minutes = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue and fresh_oranges > 0:
        minutes += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (
                    0 <= new_x < rows
                    and 0 <= new_y < cols
                    and grid[new_x][new_y] == 1
                ):
                    grid[new_x][new_y] = 2
                    fresh_oranges -= 1
                    queue.append((new_x, new_y))

    return minutes if fresh_oranges == 0 else -1

ans = orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
print(ans)
   
#flood fill leetcode problem
from collections import deque
from copy import deepcopy

def floodFill(image, sr, sc, newColor):
    rows = len(image)
    cols = len(image[0])
    visited = deepcopy(image)
    queue = deque()
    queue.append((sr, sc))
    if image[sr][sc] == newColor:
        return image
    while queue:
        x,y = queue.popleft()
        visited[x][y] = newColor
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and visited[new_x][new_y] == image[sr][sc]:
                queue.append((new_x, new_y))
    return visited


ans = floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
print(ans)

#detect cycle in undirected graph
from collections import deque
def has_cycle(v,e, adjacency_list):
    visited = [False] * (v + 1)
    queue = deque()
    for i in range(1,v+1):
        if visited[i]:
            continue
        queue.append((i, -1))
        visited[i] = True
        while queue:
            node, parent = queue.popleft()
            for neighbor in adjacency_list[node]:
                if not visited[neighbor]:
                    visited[neighbor]=True
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    return True
    return False   
        
adjacency_list = [
    [],
    [2,4],
    [1, 3, 6],
    [2],
    [1, 5],
    [4, 7],
    [2, 7],
    [5,6],
]
ans = has_cycle(7, 7,adjacency_list)
print(ans)

# cycle detection using DFS
def has_cycle_dfs(v,e, adjacency_list):
    visited = [False] * (v + 1)
    def dfs(node, parent):
        visited[node] = True
        for neighbor in adjacency_list[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
    for i in range(1,v+1):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False

adjacency_list = [
    [],
    [2,4],
    [1, 3, 6],
    [2],
    [1, 5],
    [4, 7],
    [2, 7],
    [5,6],
]
ans = has_cycle_dfs(7, 7,adjacency_list)
print(ans)

#nearest zero leetcode problem
from collections import deque
def nearestZero(mat):
    row = len(mat)
    col = len(mat[0])
    visited = [[0  for _ in range(col)] for _ in range(row)]
    distance = [[0  for _ in range(col)] for _ in range(row)]
    queue = deque()
    for i in range(row):
        for j in range(col):
            if mat[i][j] == 0:
                queue.append([i,j,0])
                visited[i][j] = 1
    while queue:
        i,j,d = queue.popleft()
        distance[i][j] = d
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            new_x, new_y = i + dx, j + dy
            if 0 <= new_x < row and 0 <= new_y < col and not visited[new_x][new_y]:
                visited[new_x][new_y] = 1
                queue.append([new_x, new_y, d + 1])
    return distance

matrix = [[0, 1, 0], [0, 0, 1], [0, 1, 1]]
ans = nearestZero(matrix)
print(ans)

#surrounded regions leetcode problem
def surroundedRegions(board):
    def dfs(rows, cols, board, visited, r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O" or visited[r][c]:
            return
        if visited[r][c] ==1:
            return
        if board[r][c]=="X":
            return
        visited[r][c] = 1
        dfs(rows, cols, board, visited, r - 1, c)
        dfs(rows, cols, board, visited, r, c-1)
        dfs(rows, cols, board, visited, r, c +1)
        dfs(rows, cols, board, visited, r+1, c)

    rows = len(board)
    cols = len(board[0])
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    r,c=0,0
    for c in range(cols):  
        if board[r][c]=="O":
            if visited[r][c]==0:
                dfs(rows, cols, board, visited, r, c)
    r,c=rows-1,0
    for c in range(cols):  
        if board[r][c]=="O":
            if visited[r][c]==0:
                dfs(rows, cols, board, visited, r, c)
    r,c=0,0
    for r in range(rows):
        if board[r][c]=="O":
            if visited[r][c]==0:
                dfs(rows, cols, board, visited, r, c)
    r,c=0,cols-1
    for r in range(rows):
        if board[r][c]=="O":
            if visited[r][c]==0:
                dfs(rows, cols, board, visited, r, c)

    for i in range(rows):
        for j in range(cols):
            if board[i][j]=="O" and not visited[i][j]:
                board[i][j]="X"
ans = surroundedRegions([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]])
print(ans)

#number of enclaves leetcode problem
from collections import deque
def numEnclaves(grid):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    queue = deque()
    for r in range(rows):
        for c in range(cols):
            if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and grid[r][c] == 1:
                queue.append((r,c))
                visited[r][c]=1
    while len(queue)!=0:
        r,c = queue.popleft()
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            new_x, new_y = r + dx, c + dy
            if new_x <0 or new_x<0 or new_x>=rows or new_y>=cols:
                continue
            if grid[new_x][new_y]==0:
                continue
            if grid[new_x][new_y]==1 and visited[new_x][new_y]==1:
                continue
            queue.append((new_x,new_y))
            visited[new_x][new_y]=1
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]==1 and  visited[i][j]==0:
                count+=1
    return count


ans = numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])
print(ans)

# word ladder leetcode solution TC- o(n*m*26) where m is len(newword)
from collections import deque
def wordLadder(beginWord,endWord,wordList):
    myset = set(wordList)
    if endWord not in myset:
        return 0
    queue = deque()
    queue.append((beginWord,1))
    while queue:
        currWord,level = queue.popleft()
        if currWord == endWord:
            return level
        for i in range(0,len(currWord)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c == currWord[i]:
                    continue
                newWord =currWord[:i]+c+currWord[i+1:] 
                if newWord in myset:
                    queue.append((newWord,level+1))
                    myset.remove(newWord)
    return 0

ans = wordLadder("hit","cog",["hot","dot","dog","lot","log","cog"])
print(ans)

# word ladder leetcode solution TC- o(n*m*26) where m is len(newword)
from collections import deque

def wordLadderII(beginWord, endWord, wordList):
    myset = set(wordList)

    if endWord not in myset:
        return []

    result = []
    queue = deque([[beginWord]])
    found = False

    while queue and not found:
        levelSize = len(queue)
        chosenWords = set()

        for _ in range(levelSize):
            sequence = queue.popleft()
            lastWord = sequence[-1]

            if lastWord == endWord:
                result.append(sequence)
                found = True
                continue

            for i in range(len(lastWord)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == lastWord[i]:
                        continue

                    newWord = lastWord[:i] + c + lastWord[i+1:]

                    if newWord in myset:
                        queue.append(sequence + [newWord])
                        chosenWords.add(newWord)

        for word in chosenWords:
            myset.discard(word)

    return result

ans = wordLadderII("hit","cog",["hot","dot","dog","lot","log","cog"])
print(ans)

# number of islands leetcode solution
def islands(grid):
    def dfs(r,c,base_r,base_c,shape,visited,rows,cols,grid):
        visited[r][c] = 1
        shape.append((r-base_r,c-base_c))
        for x,y in [(-1,0),(0,-1),(1,0),(0,1)]:
            new_i,new_j = r+x,y+c
            if r < 0 or r >= rows or c < 0 or c >= cols:
                continue
            if visited[r][c] ==1:
                continue
            if grid[r][c]=="0":
                continue
            dfs(new_i,new_j,base_r,base_c,shape,visited,rows,cols,grid)
    uniqueIsland = set()
    rows = len(grid)
    cols = len(grid[0])
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=="1" and visited[r][c]==0:
                shape=[]
                dfs(r,c,r,c,shape,visited,rows,cols,grid)
                uniqueIsland.add(tuple(shape))
    return len(uniqueIsland)

ans = islands([
  ["0","1","1","0","1","1"],
  ["0","0","1","0","0","0"],
  ["1","1","0","1","1","0"],
  ["0","0","0","0","1","0"]
])
print(ans)


# bipartite graph leetcode solution

def isBipartite(adjlist):
    visited=[-1 for _ in range(len(adjlist))]
    def dfs(node,color):
        visited[node]=color
        for neighbour in adjlist[node]:
            if visited[neighbour]==-1:
                if not dfs(neighbour,1-color):
                    return False
            elif visited[neighbour]==color:
                return False 
        return True
    for node in range(len(adjlist)):
        if visited[node] == -1:
            if not dfs(node, 0):
                return False
    return True

adjacency_list = [[1,3],[0,2],[1,3],[0,2]]
ans = isBipartite(adjacency_list)
print(ans)