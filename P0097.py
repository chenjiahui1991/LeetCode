class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False
        f = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m):
            if s1[i] == s3[i]:
                f[i + 1][0] = True
            else:
                break
        for i in range(n):
            if s2[i] == s3[i]:
                f[0][i + 1] = True

        for i in range(m + 1):
            for j in range(n + 1):
                if (i > 0 and s1[i - 1] == s3[i + j - 1] and f[i - 1][j]) or (j > 0 and s2[j - 1] == s3[i + j - 1] and f[i][j - 1]):
                    f[i][j] = True
        return f[m][n]



s = Solution()
print(s.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
