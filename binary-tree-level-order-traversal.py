class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def levelOrder(root):
	mapper = {}
	res = []
	def traverse(root, level):
		if level not in mapper:
			mapper[level] = []
		if root:
			mapper[level].append(root.val)
			
			if root.left: traverse(root.left, level+1)
			if root.right: traverse(root.right, level+1)
	traverse(root, 0)
	for key in mapper:
		res.append(mapper[key])

	return res

root = TreeNode(3)

print(levelOrder(root))