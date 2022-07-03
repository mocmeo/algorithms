class TreeNode(object):
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def maxPathSum(root):
	res = [root.val]
	def dfs(root):
		if not root:
			return 0
		if root:
			leftMax = max(dfs(root.left), 0)
			rightMax = max(dfs(root.right), 0)

			# with split
			res[0] = max(res[0], root.val + leftMax + rightMax)

			# without split
			return root.val + max(leftMax, rightMax)
	dfs(root)
	return res[-1]


root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(maxPathSum(root))