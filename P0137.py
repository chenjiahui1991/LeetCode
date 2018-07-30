import numpy as np

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in range(32):
            tmp = 0
            for num in nums:
                tmp += (1 << i) & num
            if tmp % 3 != 0:
                result += 1 << i
        x = np.array(result, dtype=np.int32)
        return x.tolist()






s = Solution()
print(s.singleNumber([2,2,3,2]))
print(s.singleNumber([0,1,0,1,0,1,99]))
print(s.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2]))
