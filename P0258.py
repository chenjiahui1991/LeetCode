class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            tmp = num
            num = 0
            while tmp > 0:
                num += tmp % 10
                tmp //= 10
        return num


s = Solution()
print(s.addDigits(38))
