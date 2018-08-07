class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        if len(nums) == 0: return []
        left, right = nums[0], nums[0]
        nums.append(nums[-1] + 2)
        for val in nums[1:]:
            if val == right + 1:
                right += 1
            else:
                if left == right:
                    result.append(str(left))
                else:
                    result.append(str(left) + '->' + str(right))
                left, right = val, val
        return result


s = Solution()
print(s.summaryRanges([0,1,2,4,5,7]))
print(s.summaryRanges([0,2,3,4,6,8,9]))

