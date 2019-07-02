class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def leafSimilar(root1, root2):
    leaves1 = dfs(root1, [])
    leaves2 = dfs(root2, [])
    return leaves1 == leaves2


def dfs(root, leaves):
    if root:
        if (not root.left and not root.right):
            leaves.append(root.val)
        dfs(root.left, leaves)
        dfs(root.right, leaves)
    return leaves


root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(9)
root.right.right = TreeNode(8)

leafSimilar(root, root)
