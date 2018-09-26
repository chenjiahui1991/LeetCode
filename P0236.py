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
        path1 = []
        path2 = []

        def calcDepth(root, subStr, p, q):
            subStr.append(root.val)
            nonlocal path1, path2
            if root.val == p.val:
                path1 = subStr[:]
            if root.val == q.val:
                path2 = subStr[:]
            if root.left is not None: calcDepth(root.left, subStr, p, q)
            if root.right is not None: calcDepth(root.right, subStr, p, q)
            subStr.pop()


        calcDepth(root, [], p, q)

        ourPath = []
        for i in range(min([len(path1), len(path2)])):
            if path1[i] == path2[i]:
                ourPath.append(path1[i])

        def findNode(root, ourPath):
            if len(ourPath) == 1:
                return root
            else:
                ourPath.pop(0)
                if root.left is not None and root.left.val == ourPath[0]:
                    return findNode(root.left, ourPath)
                else:
                    return findNode(root.right, ourPath)

        return findNode(root, ourPath)





root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
s = Solution()
print(s.lowestCommonAncestor(root, TreeNode(2), TreeNode(6)).val)
# print(s.lowestCommonAncestor(root, TreeNode(2), TreeNode(4)))

# t = []
# t.extend([1])
# print(t)
