class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preSuc(root,num):
    current = root
    sucessor=None
    while current:
        if  current.val > num:
            sucessor=current.val
            current = current.left
        else:
            current = current.right
    return sucessor

ans = preSuc(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))), 3)
print(ans)