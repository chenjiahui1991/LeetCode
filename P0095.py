# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def print(self, root, result):
        if root != None:
            result.append(root.val)
            self.print(root.left, result)
            self.print(root.right, result)

    def copyTree(self, node):
        if node == None:
            return None
        result = TreeNode(node.val)
        result.left = self.copyTree(node.left)
        result.right = self.copyTree(node.right)
        return result

    def dfs(self, cands):
        if len(cands) == 0:
            return [None]
        result = []
        for i in range(len(cands)):
            left = self.dfs(cands[:i])
            right = self.dfs(cands[i + 1:])
            for m in range(len(left)):
                for n in range(len(right)):
                    root = TreeNode(cands[i])
                    root.left = left[m]
                    root.right = right[n]
                    result.append(self.copyTree(root))
        return result

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.dfs([i for i in range(1, n + 1)])

s = Solution()
lists = s.generateTrees(3)
for root in lists:
    result = []
    s.print(root, result)
    print(result)
