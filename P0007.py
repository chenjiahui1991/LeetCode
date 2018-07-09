class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        min_val = -2 ** 31
        max_val = 2 ** 31 - 1
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = x * sign
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x = x // 10
        result = sign * result
        if min_val <= result <= max_val:
            return result
        else:
            return 0



s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
print(s.reverse(-2 ** 31))

