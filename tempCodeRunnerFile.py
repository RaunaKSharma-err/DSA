# power bits

n = [1, 2, 3, 4]
length = len(n)
subsets = 1 << length
res = []

for nums in range(0, subsets):
    lst = []
    for i in range(0, length):
        if nums & (1 << i) != 0:
            print(nums, i)
            lst.append(nums[i])
        res.append(lst)
print(res)
