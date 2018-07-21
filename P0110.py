# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getLevel(self, root):
        if root == None: return 0
        left = self.getLevel(root.left)
        right = self.getLevel(root.right)
        if left == float('inf') or right == float('inf') or abs(left - right) > 1:
            return float('inf')
        return max(left, right) + 1


    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        return self.getLevel(root) != float('inf')


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
s = Solution()
print(s.isBalanced(root))
