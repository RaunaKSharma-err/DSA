class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deleteNode(root,key):
    temp = root
    if not root:
        return None
    while temp and temp.val != key:
        if temp.val == key:
            if temp.right:
                while temp.right:
                    temp.val = temp.right.val
                    temp = temp.right
            else:
                while temp.left:
                    temp.val = temp.left.val
                    temp = temp.left
            temp.val = None
        elif temp.val < key:
            temp = temp.right
        else: 
            temp = temp.left
    return root
        
ans = deleteNode(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))), 3)
print(ans)