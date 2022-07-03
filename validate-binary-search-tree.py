class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def isValidBST(root, minVal=float('-inf'), maxVal=float('inf')):
	if root is None:
		return True
	if root.val <= minVal or root.val >= maxVal:
		return False

	return isValidBST(root.left, minVal, root.val) and isValidBST(root.right, root.val, maxVal)

root = TreeNode(0)
root.left = TreeNode(-1)
print(isValidBST(root))