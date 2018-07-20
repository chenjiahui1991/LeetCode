class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if s[0] == '0':
            return 0
        f = [0] * len(s)
        f[0] = 1
        for i in range(1, len(s)):
            if s[i] != '0':
                f[i] += f[i - 1]
            if 10 <= int(s[i - 1: i + 1]) <= 26:
                if i >= 2:
                    f[i] += f[i - 2]
                else:
                    f[i] += 1
        return f[-1]




s = Solution()
print(s.numDecodings("101"))

