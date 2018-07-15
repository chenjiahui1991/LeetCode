class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        far = 0
        maxStep = nums[0]
        for i, val in enumerate(nums):
            if i == far:
                maxStep = max(maxStep, i + val)
                far = maxStep
                if far == i and i != len(nums) - 1:
                    return False
            else:
                maxStep = max(maxStep, i + val)
            # print(result, far, maxStep)
        return True

s = Solution()
print(s.canJump([2,0,0]))
