class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[-1] > nums[0]:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[-1]:
                left = mid + 1
            else: right = mid
        return min(nums[left], nums[right])


s = Solution()
print(s.findMin([2,2,2,0,1]))
print(s.findMin([1,3,5]))
print(s.findMin([3,1,3]))
