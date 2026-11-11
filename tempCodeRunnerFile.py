def minimumCost(cost1, cost2, costBoth, need1, need2):
    both = min(need1, need2)
    cost_a = both * min(costBoth, cost1 + cost2)+(need1 - both) * cost1+(need2 - both) * cost2
    cost_b = max(need1, need2) * costBoth
    return min(cost_a, cost_b)
print(minimumCost(3,2,1,3,2))