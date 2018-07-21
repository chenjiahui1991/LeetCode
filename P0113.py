# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def existsSum(self, root, sum, target, subset, set):
        if root.left == None and root.right == None:
            if sum + root.val == target:
                set.append(subset[:])
                set[-1].append(root.val)
            return
        if root.left != None:
            subset.append(root.val)
            self.existsSum(root.left, sum + root.val, target, subset, set)
            subset.pop()
        if root.right != None:
            subset.append(root.val)
            self.existsSum(root.right, sum + root.val, target, subset, set)
            subset.pop()

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []
        if root == None:
            return []
        self.existsSum(root, 0, sum, [], result)
        return result


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
s = Solution()
print(s.pathSum(root, 12))
