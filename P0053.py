class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        left = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum > result:
                result = sum
            while sum <= 0 and left <= i:
                sum -= nums[left]
                left += 1
        return result


s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
