def majorityElement(nums , target):
    for i in range(len(nums)):
        ans=[]
        for j in range(0,len(nums)):
            if len(ans)> i:
                ans.pop()
            ans.append(nums[j])
            print(ans)


ans = majorityElement([1,2,2,3],2)
print(ans)