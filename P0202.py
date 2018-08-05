class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mem = set()
        while n not in mem:
            mem.add(n)
            tmp = 0
            while n > 0:
                tmp += (n % 10) ** 2
                n //= 10
            n = tmp
        return n == 1


s = Solution()
print(s.isHappy(19))

