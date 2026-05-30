def minimumPlatform(arr, dep):
    arr.sort()
    dep.sort()
    platform_needed = 1
    max_platforms = 1
    j = 0
    i = 1
    while i < len(arr) and j < len(dep):
        if arr[i] <= dep[j]:
            platform_needed += 1
            i += 1
        else:
            platform_needed -= 1
            j += 1
        max_platforms = max(max_platforms, platform_needed)
    return max_platforms


ans = minimumPlatform(
    [900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]
)
print(ans)