class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs_left(root, visited):
    if root:
        visited.append(root.val)
        dfs_left(root.left, visited)
        dfs_left(root.right, visited)
    else:
        visited.append(root)
    return visited


def dfs_right(root, visited):
    if root:
        visited.append(root.val)
        dfs_right(root.right, visited)
        dfs_right(root.left, visited)
    else:
        visited.append(root)
    return visited


def isSymmetric(root):
    leftTraversal = dfs_left(root, [])
    rightTraversal = dfs_right(root, [])
    print(leftTraversal)
    print(rightTraversal)
    return leftTraversal == rightTraversal


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(isSymmetric(root))
