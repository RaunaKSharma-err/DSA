def maximumSaleItems(items, budget):
    n = len(items)
    def recursion(index,budgets):
        if index == n:
            return 0
        price = items[index][1]
        factor= items[index][0]
        no_of_copies = budgets//price
        max_items = 0
        for copies in range(no_of_copies+1):
            free_copies = 0
            remaining = budgets-(copies*price)
            if copies > 0:
                for j in range(n):
                    if items[j][0] % factor == 0 and j != index:
                        free_copies += 1  
            current = free_copies + copies + recursion(index+1,remaining)
            max_items = max(max_items,current)            
        return max_items

    dp = dp = [[-1] * (budget + 1) for _ in range(n)]
    def memoization(index,budgets):
        if index == n:
            return 0
        if dp[index][budgets]!=-1:
            return dp[index][budgets]
        price = items[index][1]
        factor= items[index][0]
        no_of_copies = budgets//price
        max_items = 0
        for copies in range(no_of_copies+1):
            free_copies = 0
            remaining = budgets-(copies*price)
            if copies > 0:
                for j in range(n):
                    if items[j][0] % factor == 0 and j != index:
                        free_copies += 1  
            current = free_copies + copies + memoization(index+1,remaining)
            max_items = max(max_items,current)            
        dp[index][budgets] = max_items
        return dp[index][budgets]

    def tabulation(items,budgets):
        dp = [[0] * (budgets + 1) for _ in range(n + 1)]
        for index in range(n - 1, -1, -1):
            price = items[index][1]
            factor = items[index][0]
            for b in range(budgets + 1):
                no_of_copies = b // price
                max_items = 0
                for copies in range(no_of_copies + 1):
                    free_copies = 0
                    remaining = b - copies * price
                    if copies > 0:
                        for j in range(n):
                            if items[j][0] % factor == 0 and j != index:
                                free_copies += 1
                    current = free_copies + copies + dp[index + 1][remaining]
                    max_items = max(max_items, current)
                dp[index][b] = max_items
        return dp[0][budgets]
        
    def spaceOptimization(items,budgets):
        prev = [0 for _ in range(budgets+1)]
        for index in range(n - 1, -1, -1):
            price = items[index][1]
            factor = items[index][0]
            curr = [0 for _ in range(budgets+1)]
            for b in range(budgets + 1):
                no_of_copies = b // price
                max_items = 0
                for copies in range(no_of_copies + 1):
                    free_copies = 0
                    remaining = b - copies * price
                    if copies > 0:
                        for j in range(n):
                            if items[j][0] % factor == 0 and j != index:
                                free_copies += 1
                    current = free_copies + copies + prev[remaining]
                    max_items = max(max_items, current)
                curr[b] = max_items
            prev = curr
        return prev[budgets]
    
    return spaceOptimization(items,budget)

print(maximumSaleItems([[6,2],[2,6],[3,4]],9))