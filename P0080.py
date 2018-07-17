class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        left = 1
        current = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == current:
                count += 1
                if count <= 2:
                    nums[left] = nums[i]
                    left += 1
            else:
                current = nums[i]
                count = 1
                nums[left] = nums[i]
                left += 1
        return left

s = Solution()
nums = [0,0,1,1,1,1,2,3,3]
print(s.removeDuplicates(nums))
print(nums)
