class solution:
    def cielthefloor(self, nums, target):
        low = 0
        high = len(nums) - 1
        if target <= nums[len(nums) - 1]:
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < nums[high]:
                    if nums[mid] < target < nums[high]:
                        low = mid + 1
                    else:
                        high = mid - 1
                elif nums[low] < nums[mid]:
                    if nums[low] < target < nums[mid]:
                        high = mid - 1
                    else:
                        low = mid + 1
        return -1


nums = [11, 15, 20, 1, 4, 5, 6, 8, 9, 10]
c = solution()
x = c.cielthefloor(nums, 20)
print(x)
