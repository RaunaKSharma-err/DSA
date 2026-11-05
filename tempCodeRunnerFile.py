def findTheDistanceValue(arr1,arr2,d):
    count=0
    for i in range(len(arr1)):
        valid = True
        for j in range(len(arr2)):
            if abs(arr1[i]-arr2[j]) <= d:
                valid= False
                break
        if valid:
            count+=1
    return count
print(findTheDistanceValue([4,5,8],[10,9,1,8],2))