def PartitionEqualSubsetSum(nums , target):
    def Recursion(index,total):
        if index >= len(nums):  
            return target == total            
        pick = Recursion(index + 1, total+ nums[index])
        notPick = Recursion(index + 1, total)
        return pick or notPick

    dp = [[False for _ in range(len(nums))]for _ in range(target)]
    def Memoization(index,total):
        if total == 0:
            return True
        if index == 0:
            if nums[0] == total:
                return True
        if dp[index][total] != False:
            return True
        if nums[index] > total:
            pick = False
        else:
            pick = Memoization(index + 1, total+ nums[index])
        notPick = Memoization(index + 1, total)
        dp[index][total] =  pick or notPick
        return dp[index][total]

    def Tabulation():
        pass
    return Memoization(0,0)

nums = [1,5,11,5]
target = sum(nums)//2
print(PartitionEqualSubsetSum(nums,target))