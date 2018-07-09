class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        delta = abs(nums[0] + nums[1] + nums[2] - target)
        result = nums[0] + nums[1] + nums[2]
        nums = sorted(nums)
        lasti = nums[0] - 1
        for i, val1 in enumerate(nums[: -2]):
            if lasti == val1:
                continue
            lasti = val1
            left, right = i + 1, len(nums) - 1
            while left < right:
                tmp = val1 + nums[left] + nums[right] - target
                if abs(tmp) < delta:
                    delta = abs(tmp)
                    result = val1 + nums[left] + nums[right]
                if tmp < 0:
                    left = left + 1
                elif tmp > 0:
                    right = right - 1
                else:
                    return result
        return result

s = Solution()
print(s.threeSumClosest([-3,-2,-5,3,-4], -1))


