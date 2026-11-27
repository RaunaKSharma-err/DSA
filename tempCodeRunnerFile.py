def maximumSaleItems(items, budget):
    return sorted(items,key=lambda row:row[1])

print(maximumSaleItems([[12, 4],[2, 4], [3, 2], [4, 1], [6, 4]],8))