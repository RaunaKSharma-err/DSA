class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lcm(root,p,q):
   current = root
   while True:
        if current.val < p and current.val < q:
           current = current.right
        elif current.val > p and current.val > q:
           current = current.left
        elif p == current.val:
            return p
        elif q== current.val:
            return q
        else:
            return current

ans = lcm(TreeNode(6,TreeNode(2,TreeNode(0),TreeNode(4,TreeNode(3),TreeNode(5))),TreeNode(8,TreeNode(7),TreeNode(9))),2,8)
print(ans)