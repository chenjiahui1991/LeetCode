from functools import cmp_to_key
import operator

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(lambda x, y: 1 if operator.gt((y+x),(x+y)) else -1))
        result = "".join(nums)
        result = result.lstrip('0')
        if len(result) == 0: result = '0'
        return result


s = Solution()
# print(s.largestNumber([10,2]))
# print(s.largestNumber([3,30,34,5,9]))
print(s.largestNumber([0, 0]))
