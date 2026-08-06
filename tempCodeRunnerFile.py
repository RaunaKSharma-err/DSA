def findMinimumBst(root):
    while root.left.left:
        root = root.left
    return root.left.val - root.left.left.val
ans = findMinimumBst([4,2,6,1,3])
print(ans)