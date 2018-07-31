class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        while n > 0:
            n = n - 1
            tmp = n % 26
            result = chr(ord('A') + tmp) + result
            n //= 26
        return result


s = Solution()
print(s.convertToTitle(1))
print(s.convertToTitle(28))
print(s.convertToTitle(701))
