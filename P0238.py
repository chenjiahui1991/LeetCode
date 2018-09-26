class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1 for _ in range(len(nums))]
        tmp = 1
        for i in range(len(nums)):
            result[i] *= tmp
            tmp *= nums[i]
        tmp = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= tmp
            tmp *= nums[i]
        return result

s = Solution()
print(s.productExceptSelf([1,2,3,4]))
