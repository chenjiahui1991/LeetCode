class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        total = sum(nums)
        if total < s: return 0
        left, point = 0, 0
        value = 0
        result = len(nums)
        while point < len(nums):
            while point < len(nums) and value < s:
                value += nums[point]
                point += 1
            while left < point and value - nums[left] >= s:
                value -= nums[left]
                left += 1
            if value >= s and point - left < result:
                result = point - left
            value -= nums[left]
            left += 1
        return result

s = Solution()
print(s.minSubArrayLen(5, [1,1,1,1,1,3,2]))
