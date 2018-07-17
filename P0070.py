class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        last1 = 1
        last2 = 2
        for i in range(3, n + 1):
            tmp = last1 + last2
            last1 = last2
            last2 = tmp
        return last2


s = Solution()
print(s.climbStairs(3))
