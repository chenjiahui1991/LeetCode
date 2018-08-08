from utils import constructTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        m = p.val
        n = q.val
        if m == n: return p
        if m > n: m, n = n, m
        def findCommon(node, p, q):
            if p == node.val or q == node.val: return node
            if p < node.val and q > node.val: return node
            if q < node.val: return findCommon(node.left, p, q)
            return findCommon(node.right, p, q)
        return findCommon(root, m, n)


# root = constructTree([6,2,8,0,4,7,9,None,None,3,5])
# s = Solution()
# print(s.lowestCommonAncestor(root, TreeNode(2), TreeNode(8)))
# print(s.lowestCommonAncestor(root, TreeNode(2), TreeNode(4)))
root = constructTree([2, 1, 3])
s = Solution()
print(s.lowestCommonAncestor(root, TreeNode(3), TreeNode(1)).val)
# print(s.lowestCommonAncestor(root, TreeNode(2), TreeNode(4)))
