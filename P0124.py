from utils import constructTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMaxValue(self, node):
        self.maxSingleValue = max(self.maxSingleValue, node.val)
        values = [node.val]
        allValue = node.val
        if node.left is not None:
            leftValue = self.getMaxValue(node.left)
            values.append(leftValue + node.val)
            allValue += leftValue
        if node.right is not None:
            rightValue = self.getMaxValue(node.right)
            values.append(rightValue + node.val)
            allValue += rightValue
        result = max(values)
        if self.result < max(result, allValue):
            self.result = max(result, allValue)
        return max(result, 0)

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = root.val
        self.maxSingleValue = root.val
        self.getMaxValue(root)
        return self.result if self.maxSingleValue >= 0 else self.maxSingleValue



root = constructTree([1,-2,-3,1,3,-2,None,-1])
s = Solution()
print(s.maxPathSum(root))

