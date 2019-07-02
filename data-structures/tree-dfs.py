# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        visited_p = self.dfs(p, [])
        visited_q = self.dfs(q, [])
        return visited_p == visited_q

    def dfs(self, root, visited):
        if root:
            visited.append(root.val)
            self.dfs(root.left, visited)
            self.dfs(root.right, visited)
        else:
            visited.append(root)
        return visited
