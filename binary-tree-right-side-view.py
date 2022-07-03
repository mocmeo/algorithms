class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def rightSideView(root):
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
		if len(mapper[key]):
			res.append(mapper[key][-1])

	return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

print(rightSideView(root))