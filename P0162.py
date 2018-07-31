class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0
        if nums[0] > nums[1]: return 0
        if nums[-1] > nums[-2]: return len(nums) - 1
        left, right = 1, len(nums) - 2
        while left < right:
            mid = (left + right) >> 1
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] < nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
        return left


s = Solution()
print(s.findPeakElement([1,2,1,3,5,6,4]))
print(s.findPeakElement([1,2,3,1]))
