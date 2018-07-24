class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(t) == 0 or len(s) == 0:
            return 0
        m = len(s)
        n = len(t)
        f = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        f[0][0] = 1
        tmp = []
        for i in range(n):
            mem = tmp
            tmp = [0 for _ in range(m + 1)]
            for j in range(i, m):
                if t[i] == s[j]:
                    if i == 0:
                        f[i + 1][j + 1] = 1
                    else:
                        f[i + 1][j + 1] += mem[j]
                tmp[j + 1] = tmp[j] + f[i + 1][j + 1]
        return sum(f[-1])


s = Solution()
print(s.numDistinct("rabbbit", "rabbit"))
print(s.numDistinct("babgbag", "bag"))
