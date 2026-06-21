
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
    ans=[]
    while queue:
        node = queue.popleft()
        ans.append(node)
        for neighbour in adj_list[node]:
            indegrees[neighbour] -= 1
            if indegrees[neighbour] == 0:
                queue.append(neighbour)
    return ans

ans = CourseSchedule2(4,[[1,0],[2,0],[3,1],[3,2]])
print(ans)