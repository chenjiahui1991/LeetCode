# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(postorder) == 0:
            return None
        result = TreeNode(postorder[-1])
        ind = inorder.index(postorder[-1])
        result.left = self.buildTree(inorder[: ind], postorder[: ind])
        result.right = self.buildTree(inorder[ind + 1 :], postorder[ind : -1])
        return result

s = Solution()
print(s.buildTree([9,3,15,20,7], [9,15,7,20,3]))
