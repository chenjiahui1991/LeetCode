# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    a = None
    b = None
    previousValue = -float('inf')

    def dfs(self, node):
        if node != None:
            if self.dfs(node.left):
                return
            if node.val < self.previousValue:
                if self.b == None:
                    self.b = node
                else:
                    self.b = node
                    return True
            if self.b == None:
                self.a = node
            self.previousValue = node.val
            if self.dfs(node.right):
                return

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.dfs(root)
        print(self.a.val, self.b.val)
        tmp = self.a.val
        self.a.val = self.b.val
        self.b.val = tmp

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)
s = Solution()
s.recoverTree(root)
