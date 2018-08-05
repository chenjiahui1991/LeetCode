class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        template = (2 ** 31 - 1) ^ m
        tmp = m
        now = 1
        result = 0
        while tmp > 0:
            last = tmp & 1
            if last == 1 and m + (template & (2 ** now - 1)) + 1 > n:
                result = result + 2 ** (now - 1)
            now += 1
            tmp = tmp >> 1
        return result


s = Solution()
print(s.rangeBitwiseAnd(5, 6))
print(s.rangeBitwiseAnd(0, 1))
