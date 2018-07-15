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
        else:
            return 1
        left, right = tag1 + 1, len(nums) - 1
        while left < right:
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left = left + 1
            right = right - 1

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        while True:
            result.append(nums[:])
            if self.nextPermutation(nums):
                return result

s = Solution()
print(s.permuteUnique([1,1,2]))
