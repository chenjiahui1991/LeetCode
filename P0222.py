from utils import constructTree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        def getMostLeftNumber(node, number):
            if node.left == None:
                return number
            return getMostLeftNumber(node.left, 2 * number - 1)
        node = root
        number = 1
        result = 1
        while node.left is not None and node.right is not None:
            leftNumber = getMostLeftNumber(node.left, 2 * number)
            rightNumber = getMostLeftNumber(node.right, 2 * number + 1)
            if leftNumber < rightNumber:
                result = max(result, rightNumber)
                node = node.right
                number = 2 * number + 1
            else:
                result = max(result, leftNumber)
                node = node.left
                number = 2 * number
        if node.left is None and node.right is None:
                return number
        if node.left is not None and node.right is None:
            return 2 * number

        return self.result


s = Solution()
for i in range(100):
    root = constructTree(list(range(i)))
    ans = s.countNodes(root)
    if ans != i:
        print('Error:', i, ans)

