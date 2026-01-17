class solution:
    def findTheElmentInTheRotatedArray(self, nums, target):
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


nums = [10, 11, 12, 13, 1, 2, 3, 4]
c = solution()
x = c.findTheElmentInTheRotatedArray(nums, 13)
print(x)
