# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        node = TreeNode(pre[0])
        idx = post.index(pre[1])
        node.left = self.constructFromPrePost(pre[1 : idx + 2], post[: idx + 1])
        node.right = self.constructFromPrePost(pre[idx + 2 :], post[idx + 1 : -1])
        return node


pre = [1, 2, 4, 5, 3, 6, 7]
post = [4, 5, 2, 6, 7, 3, 1]
s = Solution()
node = s.constructFromPrePost(pre, post)
