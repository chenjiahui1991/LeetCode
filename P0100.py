# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def compare(self, node1, node2):
        if node1.val != node2.val:
            return False
        if (node1.left == None and node2.left != None) or (node1.left != None and node2.left == None):
            return False
        if node1.left != None and node2.left != None and self.compare(node1.left, node2.left) == False:
            return False

        if (node1.right == None and node2.right != None) or (node1.right != None and node2.right == None):
            return False
        if node1.right != None and node2.right != None and self.compare(node1.right, node2.right) == False:
            return False
        return True

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p == None and q != None) or (p != None and q == None):
            return False
        if p == None and q == None:
            return True
        return self.compare(p, q)

root1 = TreeNode(12)
root1.right = TreeNode(-60)
root2 = TreeNode(12)
root2.right = TreeNode(72)
s = Solution()
print(s.isSameTree(root1, root2))
