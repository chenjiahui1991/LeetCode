class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        base = 1
        while base <= n:
            tmp = (n // base) % 10
            if tmp == 0: result += n // base //10 * base
            elif tmp == 1: result += n // base // 10 * base + (n % base) + 1
            else: result += n // base // 10 * base + base
            base *= 10
        return result



s = Solution()
print(s.countDigitOne(1))
