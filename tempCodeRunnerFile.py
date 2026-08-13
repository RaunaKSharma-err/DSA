class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def validateBST(root):
    current = root
    while current:
        if not current.left:
            current = current.right
        else:
            # if current.left.val < root.val: 
            #     return False
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            if not predecessor.right:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                if current.val < root.val and current.left.val > current.right.val or current.val > root.val and current.left.val < current.right.val:
                    return False
                current = current.right
    return True

ans = validateBST(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)))
print(ans)