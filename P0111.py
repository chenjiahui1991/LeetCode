# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinDepth(self, root, deep, result):
        if root.left == None and root.right == None:
            if deep < result[0]:
                result[0] = deep
            return
        if root.left != None: self.getMinDepth(root.left, deep + 1, result)
        if root.right != None: self.getMinDepth(root.right, deep + 1, result)

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [float('inf')]
        if root == None: return 0
        self.getMinDepth(root, 1, result)
        return result[0]


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
s = Solution()
print(s.minDepth(root))
