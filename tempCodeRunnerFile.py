def minimumPlatform(arr, dep):
    max_platform = 0
    n = len(arr)
    for i in range(n):
        platform=1
        for j in range(n):
            if arr[i] < dep[j] < dep[i]:
                platform += 1
        max_platform = max(max_platform, platform)
    return max_platform

ans = minimumPlatform(
    [900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]
)
print(ans)