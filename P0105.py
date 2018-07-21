# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None
        result = TreeNode(preorder[0])
        ind = inorder.index(preorder[0])
        result.left = self.buildTree(preorder[1 : ind + 1], inorder[: ind])
        result.right = self.buildTree(preorder[ind + 1 :], inorder[ind + 1 :])
        return result

s = Solution()
print(s.buildTree([3,9,20,15,7], [9,3,15,20,7]))
