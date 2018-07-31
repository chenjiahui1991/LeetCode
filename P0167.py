class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binary_search(nums, val):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) >> 1
                if nums[mid] == val: return mid
                if nums[mid] < val: left = mid + 1
                else: right = mid - 1
            return -1

        for i in range(len(numbers)):
            j = binary_search(numbers[i + 1 :], target - numbers[i])
            if j != -1: return [i + 1, i + 1 + j + 1]


s = Solution()
print(s.twoSum([2,7,11,15], 9))
