def minMoves(nums):
    maxi = max(nums)
    return sum(maxi-num for num in nums)
print(minMoves([2,1,3]))