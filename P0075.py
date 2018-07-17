class Solution:
    def swap(self, a, b):
        return b, a

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left, right = -1, len(nums)
        point = 0
        while point < right:
            if nums[point] == 0:
                left += 1
                if left == point:
                    point += 1
                else:
                    nums[left], nums[point] = self.swap(nums[left], nums[point])
            elif nums[point] == 2:
                right -= 1
                nums[point], nums[right] = self.swap(nums[point], nums[right])
            else:
                point += 1

s = Solution()
matrix = []
s.sortColors(matrix)
print(matrix)
