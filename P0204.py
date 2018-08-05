class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        flag = [True for _ in range(n)]
        result = 0
        for i in range(2, n):
            if flag[i]:
                result += 1
                for j in range(2 * i, n, i):
                    flag[j] = False
        return result

s = Solution()
print(s.countPrimes(2))
