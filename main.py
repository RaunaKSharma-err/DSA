class solution:
    def binaarySearch(self, nums, target):
        low = 0
        high = len(nums) - 1
        if nums[high] < target:
            return len(nums)
        if nums[low] > target:
            return 0
        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        return low


nums1 = [1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13]
c = solution()
x = c.binaarySearch(nums1, 4)
print(x)
