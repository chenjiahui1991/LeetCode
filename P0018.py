class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
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
        for i, val1 in enumerate(nums[: -3]):
            if val1 == lasti:
                continue
            lasti = val1
            lastj = nums[0] - 1
            for j, val2 in enumerate(nums[i + 1 : -2]):
                if val2 == lastj:
                    continue
                lastj = val2
                lastk = nums[0] - 1
                for k, val3 in enumerate(nums[i + j + 2 : -1]):
                    if val3 == lastk:
                        continue
                    lastk = val3
                    val4 = target - val1 - val2 - val3
                    if val4 >= val3 and val4 in d and d[val4] >= [val1, val2, val3, val4].count(val4):
                        result = result + [[val1, val2, val3, val4]]
        return result


s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))


