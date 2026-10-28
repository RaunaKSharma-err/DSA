def frequencySort(s):
    hashmap = {}
    res=""
    for i in s:
        hashmap[i] = hashmap.get(i,0)+1
    sorted_hash = sorted(hashmap.items(),key=lambda x :(-x[1],x[0]))
    for ch,freq in sorted_hash:
        res+= freq*ch
    return res

print(frequencySort("tree"))