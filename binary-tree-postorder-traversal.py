class TreeNode(object):
	def __init__(self, val=0):
		self.val = val
		self.left = None
		self.right = None

def postorderTraversal(root):
	visited = []
	def traverse(root, visited):
		if root:
			if root.left: traverse(root.left, visited)
			if root.right: traverse(root.right, visited)
			visited.append(root.val)

	traverse(root, visited)
	return visited

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(postorderTraversal(root))