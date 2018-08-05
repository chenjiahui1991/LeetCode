class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        mid = (len(nums) - 1) >> 1
        left, right = 0, len(nums) - 1
        nums[0], nums[mid] = nums[mid], nums[0]
        while left < right:
            while left < right and nums[right] <= nums[0]: right -= 1
            while left < right and nums[left] >= nums[0]: left += 1
            nums[left], nums[right] = nums[right], nums[left]
        nums[left], nums[0] = nums[0], nums[left]
        if k <= left + 1: return self.findKthLargest(nums[:left + 1], k)
        else: return self.findKthLargest(nums[left + 1:], k - left - 1)



s = Solution()
# print(s.findKthLargest([3,2,1,5,6,4], 2))
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
