import heapq
def findCheapestPrice(n, flights, src, dst, k):
    adj_list = [[] for _ in range(n)]
    for u,v,w in flights:
        adj_list[u].append([v,w])
    heap = [(0, src, 0)]
    dist = [[float('inf')] * (k + 2) for _ in range(n)]
    dist[src][0] = 0
    while heap:
        cost, node, stops = heapq.heappop(heap)
        if node == dst:
            return cost
        if stops == k + 1:
            continue
        for nei, price in adj_list[node]:
            new_cost = cost + price
            if new_cost < dist[nei][stops + 1]:
                dist[nei][stops + 1] = new_cost
                heapq.heappush(heap, (new_cost, nei, stops + 1))
    return -1

ans = findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0)
print(ans)