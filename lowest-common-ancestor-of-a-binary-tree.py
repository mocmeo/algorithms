class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def lowestCommonAncestor(root, p, q):
	parent = {}
	parent[root] = None
	def traverse(root):
		if root:
			if root.left: 
				parent[root.left] = root
				traverse(root.left)
			if root.right:
				parent[root.right] = root
				traverse(root.right)

	traverse(root)
	ancestors = set({})
	while p:
		ancestors.add(p)
		p = parent[p]

	while q and q not in ancestors:
		q = parent[q]
	return q

root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
p = root.left
q = root.right

print(lowestCommonAncestor(root, p, q))

