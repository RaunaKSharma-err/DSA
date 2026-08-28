def backtrack(res,index,sum):
    if index >=len(nums) or sum < 0:
        return
    if sum == 0:
        result.append(res.copy())
        return
    res.append(nums[index])
    sum -= nums[index]
    backtrack(res,index,sum)
    sum += nums[index]
    res.pop()
    backtrack(res,index+1,sum) 

nums = [2,3,6,7]
target=7
result=[]
backtrack([],0,7)
print(result)