import heapq,sys
def shortestWays(n, roads):
    MOD = 10**9+7
    adj_list = [[] for _ in range(n)]
    for u ,v ,w in roads:
        adj_list[u].append([v,w])
        adj_list[v].append([u,w])
    distance = [sys.maxsize for _ in range(n)]
    ways = [0 for _ in range(n)]
    distance[0]=0
    ways[0]=1
    priority_queue = [[0,0]]
    while priority_queue:
        dist,node = heapq.heappop(priority_queue)
        for neighbor,weight in adj_list[node]:
            new_dist = dist+weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(priority_queue,[new_dist,neighbor])
                ways[neighbor] = ways[node]
            elif new_dist == distance[neighbor]:
                ways[neighbor]=(ways[neighbor]+ways[node])%MOD
    return ways[n-1]%MOD
ans = shortestWays(7,[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]])
print(ans)