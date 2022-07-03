class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def serialize(root):
	res = []
	def traverse(root, res):
		if root:
			res.append(root.val)
			traverse(root.left, res)
			traverse(root.right, res)
		else:
			res.append("*")
	traverse(root, res)
	seri = " ".join(str(x) for x in res)
	return seri

def build_tree(pre):
	rootVal = pre.pop(0)
	if rootVal == '*':
		return None

	root = TreeNode(int(rootVal))
	root.left = build_tree(pre)
	root.right = build_tree(pre)
	return root

def deserialize(data):
	arr = data.split(" ")
	return build_tree(arr)

	

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
root.right.right.left = TreeNode(6)

res = serialize(root)
tree = deserialize(res)

res = serialize(tree)
print(res)