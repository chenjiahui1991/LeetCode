class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if target < nums[0] and target > nums[-1]:
            return -1
        if nums[0] > nums[-1]:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif (target >= nums[0] and nums[0] <= nums[mid] < target) or (target <= nums[-1] and (nums[mid] >= nums[0] or nums[mid] < target)):
                    left = mid + 1
                else:
                    right = mid - 1
        else:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = left + 1
                else:
                    right = right - 1
        return -1



s = Solution()
print(s.search([1, 3, 5], 1))
