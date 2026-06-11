from collections import deque
def wordLadderII(beginWord,endWord,wordList):
    myset = set(wordList)
    ans=[]
    if endWord not in myset:
        return 0
    queue = deque()
    queue.append((beginWord,1))
    while queue:
        temp = []
        ans.append(temp)
        currWord,level = queue.popleft()
        if currWord == endWord:
            return level,ans
        for i in range(0,len(currWord)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c == currWord[i]:
                    continue
                newWord =currWord[:i]+c+currWord[i+1:] 
                if newWord in myset:
                    temp.append(newWord)
                    queue.append((newWord,level+1))
                    myset.remove(newWord)
    return 0

ans = wordLadderII("hit","cog",["hot","dot","dog","lot","log","cog"])
print(ans)