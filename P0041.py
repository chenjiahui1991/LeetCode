class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[i] < len(nums) and nums[i] >= 1 and nums[nums[i] - 1] != nums[i]:
                cur = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = cur

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1


s = Solution()
print(s.firstMissingPositive([7,8,9,11,12]))
