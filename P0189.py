class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = (len(nums) - k % len(nums)) % len(nums)
        nums[:] = (nums[k:] + nums[:k])


s = Solution()
print(s.rotate([1,2,3,4,5,6,7], 3))
print(s.rotate([-1,-100,3,99], 2))
