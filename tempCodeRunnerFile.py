def countServers(n, logs, x, queries):
    result=[]
    for query in queries:
        n = n
        hash_map= {}
        for id,time in logs:
            if query-x <= time <= query:
                if id not in hash_map:
                    hash_map[id]=1
                    n-=1
        result.append(n)
    return result

print(countServers(3,[[2,4],[2,1],[1,2],[3,1]],2,[3,4]))