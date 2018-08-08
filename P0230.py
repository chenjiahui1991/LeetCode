from utils import constructTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        def dfs(node):
            if node.left is not None:
                tmp = dfs(node.left)
                if tmp is not None: return tmp
            self.k -= 1
            if self.k == 0: return node.val
            if node.right is not None:
                tmp = dfs(node.right)
                if tmp is not None: return tmp
        return dfs(root)


root = constructTree([3,1,4,None,2])
s = Solution()
print(s.kthSmallest(root, 1))

