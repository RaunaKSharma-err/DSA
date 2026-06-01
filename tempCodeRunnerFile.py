class node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = node(5)
root.left = node(3)
root.right = node(1)
root.right.left = node(8)
root.right.right = node(7)
root.left.left = node(6)
root.left.right = node(2)


def topView(node):
    if node is None:
        return None
    queue = [(node, 0)]
    top_view = {}
    while queue:
        current_node, line = queue.pop(0)
        if line not in top_view:
            top_view[line] = current_node.val
        if current_node.left:
            queue.append((current_node.left, line - 1))
        if current_node.right:
            queue.append((current_node.right, line + 1))
    return [top_view[key] for key in sorted(top_view.keys())]


ans = topView(root)
print(ans)