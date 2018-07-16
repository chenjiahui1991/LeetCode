class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        f = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    f[i][j] = 1
                if i > 0:
                    f[i][j] += f[i - 1][j]
                if j > 0:
                    f[i][j] += f[i][j - 1]
        return f[m - 1][n - 1]

s = Solution()
print(s.uniquePaths(3, 2))
