class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def insertIntoBST(root,node):
#     if not root:
#         return TreeNode(node)
#     if root.val < node:
#         newnode = TreeNode(node)
#         newnode.left = root
#         newnode.right = root.right
#         root.right = newnode
#         root = newnode
#     else:
#         newnode = TreeNode(node)
#         newnode.right = root
#         newnode.left = root.left
#         root.left = newnode
#         root = newnode
#     return root

# ans = insertIntoBST(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 5)
# print(ans)

def insertIntoBst(root,node):
    temp = root 
    newnode = TreeNode(node)
    while temp:
        if temp.val < node:
            if temp.right is None:
                temp.right = newnode
                break
            temp = temp.right
        else:
            if temp.left is None:
                temp.left = newnode
                break
            temp = temp.left
    return root

ans = insertIntoBst(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 5)
print(ans)