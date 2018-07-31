class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        minPos = 1
        minNeg = -float('inf')
        prefix = 1
        result = nums[0]
        for num in nums:
            if num == 0:
                minPos = 1
                minNeg = -float('inf')
                prefix = 1
                continue
            else:
                prefix *= num
                result = max([result, prefix / minPos, prefix / minNeg])
                if prefix < 0 and prefix > minNeg: minNeg = prefix
        return int(result)

s = Solution()
print(s.maxProduct([2,3,-2,4]))
print(s.maxProduct([]))
print(s.maxProduct([-2,0,-1]))
