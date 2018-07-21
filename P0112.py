# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def existsSum(self, root, sum, target):
        if root.left == None and root.right == None:
            if sum + root.val == target:
                return True
            else:
                return False
        if root.left != None:
            if self.existsSum(root.left, sum + root.val, target):
                return True
        if root.right != None:
            if self.existsSum(root.right, sum + root.val, target):
                return True
        return False

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [float('inf')]
        if root == None:
            return False
        return self.existsSum(root, 0, sum)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
s = Solution()
print(s.hasPathSum(root, 12))
