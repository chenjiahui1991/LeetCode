# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def print(self, root, result):
        if root != None:
            self.print(root.left, result)
            result.append(root.val)
            self.print(root.right, result)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = []
        self.print(root, result)
        tmp = sorted(result)
        for i in range(1, len(tmp)):
            if tmp[i] == tmp[i - 1]:
                return False
        return result == tmp


root = TreeNode(1)
root.right = TreeNode(1)
s = Solution()
print(s.isValidBST(root))
