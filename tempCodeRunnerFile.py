import math
def maxLength(nums):
    n = len(nums)
    maxi = 0

    for left in range(n):
        gcd = nums[left]
        lcm = nums[left]
        product = 1

        for right in range(left, n):
            product *= nums[right]
            gcd = math.gcd(gcd, nums[right])
            lcm = math.lcm(lcm, nums[right])

            if product == gcd * lcm:
                maxi = max(maxi, right - left + 1)

    return maxi

print(maxLength([2, 3, 4, 5, 6]))