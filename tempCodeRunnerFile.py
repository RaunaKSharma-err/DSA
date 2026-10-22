def minOperations(nums):
    permutation= sorted(nums)
    if nums == permutation:
        return 0
    for i in range(1,len(nums)+1):
        move = nums[1:]
        move.append(nums[0])
        if move == permutation:
            return i
        rev = nums[::-1]
        if rev == permutation:
            return i
        nums = move
    return -1
print(minOperations([1,0,2]))