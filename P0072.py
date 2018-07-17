class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == "" or word2 == "":
            return max(len(word1), len(word2))
        word1 = word1
        word2 = word2
        mem = dict()
        f = [[float('inf') for _ in range(len(word2))] for _ in range(len(word1))]
        for i in range(len(word1)):
            for j in range(len(word2)):
                if i == 0 or j == 0:
                    f[i][j] = max(i, j) + (word1[i] != word2[j])
                    if i > 0:
                        f[i][j] = min(f[i][j], f[i - 1][j] + 1)
                    elif j > 0:
                        f[i][j] = min(f[i][j], f[i][j - 1] + 1)
                else:
                    f[i][j] = min(f[i - 1][j - 1] + (word1[i] != word2[j]), f[i - 1][j] + 1, f[i][j - 1] + 1)
        return f[-1][-1]


s = Solution()
print(s.minDistance('a', 'ab'))
