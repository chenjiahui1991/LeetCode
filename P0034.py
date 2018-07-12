class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tag1 = -1
        left, right = 0, len(nums) - 1
        while (left <= right):
            mid = (left + right) // 2
            if (nums[mid] == target and (mid == 0 or nums[mid - 1] != nums[mid])):
                tag1 = mid
                break
            elif nums[mid] < target:
                left = left + 1
            else:
                right = right - 1
        if tag1 == -1:
            return [-1, -1]
        left, right = tag1, len(nums) - 1
        while (left <= right):
            mid = (left + right) // 2
            if (nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] != nums[mid])):
                return [tag1, mid]
            elif nums[mid] > target:
                right = right - 1
            else:
                left = left + 1



s = Solution()
print(s.searchRange([5,7,7,8,8,10], 11))
