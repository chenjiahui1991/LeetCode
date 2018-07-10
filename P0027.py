class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        point = -1
        for v in nums:
            if v != val:
                point = point + 1
                nums[point] = v
        return point + 1

s = Solution()
print(s.strStr("", ""))

