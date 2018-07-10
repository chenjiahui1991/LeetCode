class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        point = 0
        for val in nums[1 :]:
            if val != nums[point]:
                point = point + 1
                nums[point] = val
        # print(nums)
        return point + 1

s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

