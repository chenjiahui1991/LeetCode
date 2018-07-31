# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(deep, node):
            mem[deep] = node.val
            if node.left is not None: dfs(deep + 1, node.left)
            if node.right  is not None: dfs(deep + 1, node.right)
        if root is None: return []
        mem = dict()
        dfs(0, root)
        result = []
        for i in range(max(list(mem.keys())) + 1):
            result.append(mem[i])
        return result



root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.right = TreeNode(4)

s = Solution()
print(s.rightSideView(root))

