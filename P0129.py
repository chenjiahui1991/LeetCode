from utils import constructTree

class Solution:
    def dfs(self, root, value):
        if root.left is None and root.right is None:
            self.result += value * 10 + root.val
            return
        if root.left is not None:
            self.dfs(root.left, value * 10 + root.val)
        if root.right is not None:
            self.dfs(root.right, value * 10 + root.val)


    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        if root is None:
            return 0
        self.dfs(root, 0)
        return self.result



root = constructTree([4,9,0,5,1])
s = Solution()
print(s.sumNumbers(root))
