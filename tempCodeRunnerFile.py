def coinChange(coins, amount):
    coinSet = []
    coins.sort(reverse=True)
    for coin in coins:
        while amount >= coin:
            amount -= coin
            coinSet.append(coin)

    if amount == 0:
        return coinSet
    return []


coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
amount = 43
ans = coinChange(coins, amount)
print(ans)