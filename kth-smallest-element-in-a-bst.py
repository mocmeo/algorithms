class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def kthSmallest(root, k):
	stack = []
	def traverse(root):
		if root.left: traverse(root.left)
		stack.append(root.val)
		if root.right: traverse(root.right)
	traverse(root)
	return stack[k-1]


root = TreeNode(5)
root.right = TreeNode(6)
root.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(1)

print(kthSmallest(root, 3))