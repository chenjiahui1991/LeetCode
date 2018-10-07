class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = n * (n + 1) // 2
        for num in nums:
            s -= num
        return s


s = Solution()
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))
