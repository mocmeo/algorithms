class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def isSameTree(p, q):
	if not p and not q:
		return True
	if p and q and p.val == q.val:
		return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
	return True

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

sroot = TreeNode(1)
sroot.left = TreeNode(2)
sroot.right = TreeNode(3)
print(isSameTree(root, sroot))