class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def sameTree(s, t):
	if not s and not t:
		return True
	if s and t and s.val == t.val:
		return (sameTree(s.left, t.left) and 
					  sameTree(s.right, t.right))
	return False

def isSubtree(root, subRoot):
	if not subRoot: return True
	if not root: return False

	if sameTree(root, subRoot):
		return True
	return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(isSubtree(root, subRoot))

