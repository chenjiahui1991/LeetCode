class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[-1] > nums[0]:
            return nums[0]
        if len(nums) == 1: return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]


s = Solution()
print(s.findMin([2,2,2,0,1]))
print(s.findMin([1,3,5]))
print(s.findMin([3, 3, 1, 3]))
print(s.findMin([3, 1, 3]))
