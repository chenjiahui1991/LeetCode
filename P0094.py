# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root, result):
        if root != None:
            self.dfs(root.left, result)
            result.append(root.val)
            self.dfs(root.right, result)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.dfs(root, result)
        return result

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
s = Solution()
print(s.inorderTraversal(root))
