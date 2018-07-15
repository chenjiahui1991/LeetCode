class Solution:
    def dfs(self, rest, candidates, index, cur, result):
        if rest == 0:
            result.append(cur[:])
            return
        for i in range(index, len(candidates)):
            if candidates[i] <= rest:
                cur.append(candidates[i])
                self.dfs(rest - candidates[i], candidates, i, cur, result)
                cur.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        result = []
        self.dfs(target, candidates, 0, [], result)
        return result



s = Solution()
print(s.combinationSum([2,3,6,7], 7))
print(s.combinationSum([2,3,5], 8))
