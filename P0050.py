class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result = 1
        if n < 0:
            x = 1 / x
            n = -n
        base = x
        while n > 0:
            if n % 2 == 1:
                result *= base
            n = n // 2
            base *= base
        return result


s = Solution()
print(s.myPow(2.0000, -2))
