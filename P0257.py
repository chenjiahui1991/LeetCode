from utils import constructTree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        if not root: return []

        def dfs(node, substring):
            if not node.left and not node.right:
                result.append(substring + str(node.val))
            else:
                if node.left:
                    dfs(node.left, substring + str(node.val) + "->")
                if node.right:
                    dfs(node.right, substring + str(node.val) + "->")

        dfs(root, "")
        return result


root = constructTree([i for i in range(7)])
s = Solution()
print(s.binaryTreePaths(root))
