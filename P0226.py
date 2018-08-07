from utils import constructTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None: return root
        tmp1 = root.left
        tmp2 = root.right
        root.left = tmp2
        root.right = tmp1
        if root.left is not None: self.invertTree(root.left)
        if root.right is not None: self.invertTree(root.right)
        return root


root = constructTree([4, 2, 7, 1, 3, 6, 9])
s = Solution()
print(s.invertTree(root))
