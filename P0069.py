import math

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.sqrt(x) // 1)


s = Solution()
print(s.mySqrt(8))
