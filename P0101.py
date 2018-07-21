# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def forward1(self, node, result):
        if node != None:
            result.append(node.val)
            self.forward1(node.left, result)
            self.forward1(node.right, result)

    def forward2(self, node, result):
        if node != None:
            self.forward2(node.left, result)
            result.append(node.val)
            self.forward2(node.right, result)

    def backward1(self, node, result):
        if node != None:
            result.append(node.val)
            self.backward1(node.right, result)
            self.backward1(node.left, result)

    def backward2(self, node, result):
        if node != None:
            self.backward2(node.right, result)
            result.append(node.val)
            self.backward2(node.left, result)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result1 = []
        result2 = []
        result3 = []
        result4 = []
        self.forward1(root, result1)
        self.backward1(root, result2)
        self.forward2(root, result3)
        self.backward2(root, result4)
        return result1 == result2 and result3 == result4

root1 = TreeNode(12)
root1.left = TreeNode(-60)
root1.right = TreeNode(-60)
s = Solution()
print(s.isSymmetric(root1))
