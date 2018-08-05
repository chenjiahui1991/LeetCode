class Solution:
    def rob_origin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        nums = [0] + nums
        f = [0 for _ in range(len(nums))]
        f[1] = nums[1]
        for i in range(2, len(nums)):
            f[i] = max(nums[i] + f[i - 2], f[i - 1])
        return f[-1]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        return max(self.rob_origin(nums[1:]), self.rob_origin(nums[:-1]))


s = Solution()
print(s.rob([1,2,3,1]))
print(s.rob([2,7,9,3,1]))
print(s.rob([]))
print(s.rob([2,3,2]))
print(s.rob([1,2,3,1]))
