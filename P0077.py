class Solution:
    def dfs(self, deep, cand, set, result):
        if deep == 0:
            result.append(set[:])
        else:
            for i in range(len(cand) - deep + 1):
                set.append(cand[i])
                self.dfs(deep - 1, cand[i + 1:], set, result)
                set.pop()

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        cand = [i for i in range(1, n + 1)]
        result = []
        self.dfs(k, cand, [], result)
        return result



s = Solution()
print(s.combine(4, 2))
