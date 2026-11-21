def findSubtreeSizes(parent, s):
    n = len(parent)
    children = [[] for _ in range(n)]
    for i in range(1, n):
        children[parent[i]].append(i)
    adj = [[] for _ in range(n)]
    last = {}
    def build(node):
        ch = s[node]
        new_parent = last.get(ch, parent[node])
        if node != 0:
            adj[new_parent].append(node)
        previous = last.get(ch)
        last[ch] = node
        for child in children[node]:
            build(child)
        if previous is None:
            del last[ch]
        else:
            last[ch] = previous
    build(0)
    ans = [1] * n
    def dfs(node):
        for child in adj[node]:
            dfs(child)
            ans[node] += ans[child]
    dfs(0)
    return ans

print(findSubtreeSizes([-1,0,0,1,1,1],"abaabc"))