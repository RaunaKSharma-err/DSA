def findTheSteps(index, total, subset, count):
    if index >= n:
        if total == 0:
            count += 1
            print(count)
        return
    if total < 0:
        return
    subset.append(1)
    sums = total - subset[index]
    findTheSteps(index + 1, sums, subset, count)
    subset[index] = 2
    sums = total - subset[index]
    findTheSteps(index + 1, sums, subset, count)


n = 5
count = 0
findTheSteps(0, 5, [], 0)
print(count)