def maxScore(cardPoints, k):
    right = -k
    maxi = 0
    arr = []
    while right < k:
        if len(arr) == k:
            arr.pop(0)
        arr.append(cardPoints[right])
        maxi = max(maxi, sum(arr))
        right += 1
    return maxi


cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3
ans = maxScore(cardPoints, k)
print(ans)