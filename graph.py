from collections import deque
from copy import deepcopy
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
# from collections import deque
# from copy import deepcopy

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
# from collections import deque
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
# from collections import deque
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
# from collections import deque
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
# from collections import deque
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
# from collections import deque

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

# process string with special operations |

def processString(val):
    res = []
    for ch in val:
        if ch == '*':
            if res:
                res.pop()
        elif ch == '#':
            res.extend(res)
        elif ch == '%':
            res.reverse()
        else:
            res.append(ch)

    return ''.join(res)
ans = processString("z*#")
print(ans)

# zigzag conversion leetcode solution

def convert(s,numRows):
    if numRows == 1 or numRows >= len(s):
            return s

    rows = [""] * numRows
    current_row = 0
    direction = 1

    for ch in s:
        rows[current_row] += ch

        if current_row == 0:
            direction = 1
        elif current_row == numRows - 1:
            direction = -1

        current_row += direction

    return "".join(rows)

# highest altitude leetcode solution

def highestAltitude(gain):
    altitude =0 
    highest=0
    for g in gain:
        altitude+=g
        highest = max(highest,altitude)
    return highest

ans = highestAltitude([-5,1,5,0,-7])
print(ans)

# detect cycle in directed graph problem

def detectCycleInDG(adj_list):
    visited = [0 for _ in range(len(adj_list))]
    pathVisited = [0 for _ in range(len(adj_list))]

    def dfs(currNode,visited,pathVisited,adj_list):
        visited[currNode]=1
        pathVisited[currNode]=1
        for neighbour in adj_list[currNode]:
            if visited[neighbour]==0:
                x=dfs(neighbour,visited,pathVisited,adj_list)
                if x==True:
                    return True
            elif pathVisited[neighbour]==1:
                return True
        pathVisited[currNode]=0
        return False

    for i in range(0,len(adj_list)):
        if visited[i]==0:
            y = dfs(i,visited,pathVisited,adj_list)
            if y == True:
                return True
    return False

adjacency_list = [
    [],
    [2],
    [3,8],
    [4,7],
    [6],
    [4],
    [],
    [5],
    [9],
    [10],[8]
]
ans = detectCycleInDG(adjacency_list)
print(ans)

# topological sort using kahns algorithm
from collections import deque
def topoSort(adj_list):
    ans=[]
    queue = deque()
    indegrees = [0 for _ in range(len(adj_list))]
    for u,v in adj_list:
        adj_list[u].append(v)
        indegrees[v]+=1
    for i in range(0,len(indegrees)):
        if indegrees[i]==0:
            queue.append(i)
    while queue:
        node = queue.popleft()
        ans.append(node)
        for neighbour in adj_list[node]:
            if indegrees[neighbour]-1==0:
                queue.append(neighbour)
            indegrees[neighbour]-=1
    return ans

adjacency_list = [
    [0,1],
    [0,2],
    [1,2],
    [2,0]
]
ans = topoSort(adjacency_list)
print(ans)

from collections import deque
def CourseSchedule2(numCourses,prerequisites):
    adj_list = [[] for _ in range(numCourses)]
    indegrees = [0] * numCourses
    for course, prereq in prerequisites:
        adj_list[prereq].append(course)
        indegrees[course] += 1
    queue = deque()
    for i in range(numCourses):
        if indegrees[i] == 0:
            queue.append(i)
    ans = []
    while queue:
        node = queue.popleft()
        ans.append(node)
        for neighbour in adj_list[node]:
            indegrees[neighbour] -= 1
            if indegrees[neighbour] == 0:
                queue.append(neighbour)
    return ans if len(ans) == numCourses else []

ans = CourseSchedule2(4,[[1,0],[2,0],[3,1],[3,2]])
print(ans)

# Eventual Safe States leetcode solution
from collections import deque
def safeNode(adjacency_list):
    ans=[]
    queue = deque()
    adj_list = [[]for _ in range(len(adjacency_list))]
    indegrees = [0 for _ in range(len(adj_list))]

    for node in range(len(adjacency_list)):
        for neighbor in adjacency_list[node]:
            adj_list[neighbor].append(node)
            indegrees[node]+=1
            
    for node in range(0,len(indegrees)):
        if indegrees[node]==0:
            queue.append(node)

    while queue:
        node = queue.popleft()
        ans.append(node)
        for neighbour in adj_list[node]:
            indegrees[neighbour] -= 1
            if indegrees[neighbour] == 0:
                queue.append(neighbour)
    return ans
adjacency_list = [
    [1,2],
    [2,3],
    [5],
    [0],
    [5],
    [],
    [],
]
ans = safeNode(adjacency_list)
print(ans)

# count subarray with majority element I

def majorityElement(nums , target):
    n = len(nums)
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + (nums[i] == target)
    ans = 0
    for l in range(n):
        for r in range(l, n):
            cnt = pref[r + 1] - pref[l]
            length = r - l + 1
            if cnt * 2 > length:
                ans += 1
    return ans
        
ans = majorityElement([1,2,2,3],2)
print(ans)

# int to roman number leetcode solution

def intToRoman(num):
    values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]
    result = ""
    for value, symbol in values:
        while num >= value:
            result += symbol
            num -= value
    return result

ans = intToRoman(51)
print(ans)

# maximum Element After Decrementing And Rearranging leetcode solution

def maximumElementAfterDecrementingAndRearranging(arr):
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            arr[i] = min(arr[i], arr[i - 1] + 1)
        return arr[-1]

# Number of Strings That Appear as Substrings in Word leetcode problem

def numberOfString(patterns,word):
    count=0
    for pattern in patterns:
        if pattern in word:
            count+=1
    return count

ans = numberOfString(["a","a","a"],"ab")
print(ans)

# sum And Multiply
def sumAndMultiply(s,queries):
    ans = []
    for l, r in queries:
        total = 0
        val = 0
        place = 1
        for ch in reversed(s[l:r+1]):
            if ch != '0':
                d = ord(ch) - ord('0') 
                total += d
                val += d * place
                place *= 10

        ans.append(total * val)
    return ans

ans = sumAndMultiply("10203004",[[0,7],[1,3],[4,6]])
print(ans)

# shortest path in undirected graph 
from collections import deque
def shortestPath(src, adjList):
    distance = [-1]*len(adjList)
    distance[src] = 0
    queue = deque([(src,0)])
    while queue:
        node,dist = queue.popleft()
        for neighbor in adjList[node]:
            if distance[neighbor]==-1:
                distance[neighbor] = dist+1
                queue.append((neighbor,dist+1))
    return distance

adjList= [
    [1,2],
    [0,2,4],
    [0,1,3],
    [2,5],
    [1,6],
    [3,6],
    [4,5,7,8],
    [6,8],
    [6,7]
]
ans = shortestPath(0,adjList)
print(ans)

# dijkstra algorithm using priority queue
import heapq
def dijkstra(edges, src):
    adjList = [[] for _ in range(len(edges))]
    for u,v,w in edges:
        adjList[u].append([v,w])
    distance = ["inf"]*len(edges)
    queue = [[src,0]]
    while queue:
        node,dist = heapq.heappop(queue)
        if distance[node]!="inf":
            continue
        distance[node] = dist
        for neighbor,weight in adjList[node]:
            if distance[neighbor]=="inf":
                heapq.heappush(queue,(neighbor,dist+weight))
    return distance

edges= [
    [0,1,4],
    [0,2,4],
    [1,0,4],
    [1,2,2],
    [2,0,4],
    [2,1,2],
    [2,3,3],
    [2,4,1],
    [2,5,6],
    [3,2,3],
    [3,5,2],
    [4,2,1],
    [4,5,3],
    [5,2,6],
    [5,3,2],
    [5,4,3]
]
ans = dijkstra(edges,0)
print(ans)

# dijkstra algorithm using set
import sys
def dijkstraSet(edges,src):
    adjList = [[] for _ in range(len(edges))]
    for u,v ,w in edges:
        adjList[u].append([v,w])
    distance = [sys.maxsize for _ in range(len(edges))]
    distance[src] = 0
    myset = set()
    myset.add((0,src))
    while len(myset) !=0:
        dist,node = min(myset)
        myset.discard((dist,node))
        for neighbor ,weight in adjList[node]:
            distanceTravel = dist+weight
            if distanceTravel < distance[neighbor]:
                if distance[neighbor]!=sys.maxsize:
                    myset.discard((distance[neighbor],neighbor))
                distance[neighbor] = distanceTravel
                myset.add((distanceTravel,neighbor))
    return distance
edges= [
    [0,1,4],
    [0,2,4],
    [1,0,4],
    [1,2,2],
    [2,0,4],
    [2,1,2],
    [2,3,3],
    [2,4,1],
    [2,5,6],
    [3,2,3],
    [3,5,2],
    [4,2,1],
    [4,5,3],
    [5,2,6],
    [5,3,2],
    [5,4,3]
]
ans = dijkstraSet(edges,0)
print(ans)

# sequential digits leetcode solution
def sequentialDigits(low, high):
    ans = []
    for start in range(1, 10):
        num = start
        for nxt in range(start + 1, 10):
            num = num * 10 + nxt
            if low <= num <= high:
                ans.append(num)
    return sorted(ans)
ans = sequentialDigits(1000,13000)
print(ans)

# shortest path using dijkstra algorithm
import heapq , sys
def shortesPath(edges, src, dest):
    adjList = [[] for _ in range(len(edges)//2)]
    path = []
    for u,v,w in edges:
        adjList[u].append([v,w])
    distance = [sys.maxsize] * len(adjList)
    parent = [-1] * len(adjList)
    priorityQueue = [[src,0]]
    parent[src] = [0]
    while priorityQueue:
        node,dist = heapq.heappop(priorityQueue)
        for neighbor,weight in adjList[node]:
            totalDist = dist+weight
            if totalDist < distance[neighbor]:
                distance[neighbor] = totalDist
                heapq.heappush(priorityQueue,(neighbor,totalDist))
                parent[neighbor] = node
    while dest != src:
        path.append(dest)
        dest = parent[dest]
    path.append(src)
    return path[::-1]


edges= [
    [1,2,2],
    [1,4,1],
    [2,1,2],
    [2,3,4],
    [2,5,5],
    [3,2,4],
    [3,4,3],
    [3,5,1],
    [4,1,1],
    [4,3,3],
    [5,2,5],
    [5,3,1],
]
ans = shortesPath(edges,1,5)
print(ans)