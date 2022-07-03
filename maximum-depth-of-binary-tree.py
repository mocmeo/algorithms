class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def maxDepth(root):
	if root:
		return max(1 + maxDepth(root.left), 1 + maxDepth(root.right))
	else:
		return 0

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(maxDepth(root))