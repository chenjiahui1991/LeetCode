# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getLeafString(self, root, result):
        if root.left == None and root.right == None:
            result.append(root.val)
            return
        if root.left != None:
            self.getLeafString(root.left, result)
        if root.right != None:
            self.getLeafString(root.right, result)

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 == None and root2 == None:
            return True
        if (root1 != None and root2 == None) or (root1 == None and root2 != None):
            return False
        str1 = []
        str2 = []
        self.getLeafString(root1, str1)
        self.getLeafString(root2, str2)
        return str1 == str2



root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(9)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
s = Solution()
print(s.leafSimilar(root, root))
