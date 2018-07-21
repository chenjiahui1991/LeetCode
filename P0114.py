# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, root):
        if root.left == None and root.right == None:
            return root, root
        last = root
        if root.left != None:
            leftHead, leftTail = self.buildTree(root.left)
        if root.right != None:
            rightHead, rightTail = self.buildTree(root.right)
        if root.left != None:
            root.left = None
            if root.right != None:
                root.right = leftHead
                leftTail.right = rightHead
                rightTail.left = None
                rightTail.right = None
                return root, rightTail
            else:
                root.right = leftHead
                leftTail.left = None
                leftTail.right = None
                return root, leftTail
        else:
            root.right = rightHead
            rightTail.left = None
            rightTail.right = None
            return root, rightTail

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None
        self.buildTree(root)



root = TreeNode(1)
root.left = TreeNode(2)
# root.right = TreeNode(5)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.right = TreeNode(6)
s = Solution()
s.flatten(root)
print(root)
