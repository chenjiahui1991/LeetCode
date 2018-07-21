# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtyp
        """
        if len(nums) == 0:
            return None
        current = len(nums) // 2
        result = TreeNode(nums[current])
        result.left = self.sortedArrayToBST(nums[:current])
        result.right = self.sortedArrayToBST(nums[current + 1:])
        return result

s = Solution()
print(s.sortedArrayToBST([-10,-3,0,5,9]))
