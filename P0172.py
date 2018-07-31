class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n > 0:
            n //= 5
            result += n
        return result



s = Solution()
print(s.trailingZeroes(1))
print(s.trailingZeroes(5))
