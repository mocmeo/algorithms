class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def invertTree(root):
	def invert(root):
		if root:
			root.left, root.right = root.right, root.left
			if root.left: invert(root.left)
			if root.right: invert(root.right)

	invert(root)
	return root

root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
print(invertTree(root))

		