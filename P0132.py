from collections import defaultdict

class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        pal_set = set()
        cands = defaultdict(list)
        for length in range(len(s)):
            for i in range(len(s) - length):
                j = i + length
                if s[i] == s[j] and (j - i <= 1 or (i + 1, j - 1) in pal_set):
                    pal_set.add((i, j))
                    cands[i].append(length)

        f = [len(s) for _ in range(len(s))]
        for length in cands[0]:
            f[length] = 0
        for i in range(1, len(s)):
            for length in cands[i]:
                f[i + length] = min(f[i + length], f[i - 1] + 1)
        return f[-1]



s = Solution()
print(s.minCut('aab'))
