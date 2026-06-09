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