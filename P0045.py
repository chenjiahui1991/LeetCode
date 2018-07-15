class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        far = 0
        maxStep = nums[0]
        result = 0
        for i, val in enumerate(nums):
            if i == far:
                maxStep = max(maxStep, i + val)
                far = maxStep
                if i != len(nums) - 1:
                    result = result + 1
            else:
                maxStep = max(maxStep, i + val)
            # print(result, far, maxStep)
        return result

s = Solution()
print(s.jump([1,2,0,1]))
