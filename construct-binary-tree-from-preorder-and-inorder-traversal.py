class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def buildTree(preorder, inorder):
	rootVal = preorder.pop(0)
	if not rootVal:
		return None
	
	root = TreeNode(rootVal)
	root.left = buildTree(preorder, inorder)
	root.right = buildTree(preorder, inorder)
	return root