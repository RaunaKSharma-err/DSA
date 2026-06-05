from collections import deque
def has_cycle(v,e, adjacency_list):
    visited = [False] * (v + 1)
    queue = deque()
    queue.append((1, -1))
    visited[1] = True
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