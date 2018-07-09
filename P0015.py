class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        d = dict()
        for val in nums:
            if val in d:
                d[val] = d[val] + 1
            else:
                d[val] = 1
        result = []
        lasti = nums[0] - 1
        for i, val1 in enumerate(nums[: -1]):
            if val1 == lasti:
                continue
            lasti = val1
            lastj = nums[0] - 1
            for j, val2 in enumerate(nums[i + 1 :]):
                if val2 == lastj:
                    continue
                lastj = val2
                val3 = -val1 - val2
                if val3 >= val2 and val3 in d and d[val3] >= [val1, val2, val3].count(val3):
                    result = result + [[val1, val2, val3]]
        return result


s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))


