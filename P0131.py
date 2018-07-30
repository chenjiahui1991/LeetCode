from collections import defaultdict

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0:
            return []
        pal_set = set()
        cands = defaultdict(list)
        for length in range(len(s)):
            for i in range(len(s) - length):
                j = i + length
                if s[i] == s[j] and (j - i <= 1 or (i + 1, j - 1) in pal_set):
                    pal_set.add((i, j))
                    cands[i].append(length)

        def dfs(s, now, subset, result):
            if now >= len(s):
                result.append(subset[:])
                return
            for length in cands[now]:
                subset.append(s[now : now + length + 1])
                dfs(s, now + length + 1, subset, result)
                subset.pop()
        result = []
        dfs(s, 0, [], result)
        return result



s = Solution()
print(s.partition('aab'))
print(s.partition(''))
