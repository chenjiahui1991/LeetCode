# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(node, result):
            if node.left is not None: dfs(node.left, result)
            if node.right is not None: dfs(node.right, result)
            result.append(node.val)

        if root == None: return []
        result = []
        dfs(root, result)
        return result


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

s = Solution()
print(s.postorderTraversal(root))
