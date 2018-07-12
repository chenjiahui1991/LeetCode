class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        tag1 = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                tag1 = i
                break;
        if tag1 != -1:
            for i in range(len(nums) - 1, -1, -1):
                if nums[tag1] < nums[i]:
                    tmp = nums[tag1]
                    nums[tag1] = nums[i]
                    nums[i] = tmp
                    break
        left, right = tag1 + 1, len(nums) - 1
        while left < right:
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left = left + 1
            right = right - 1


s = Solution()
tmp = [2, 1, 3]
s.nextPermutation(tmp)
print(tmp)

