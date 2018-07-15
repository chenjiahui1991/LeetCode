class Solution:
    def dfs(self, rest, candidates, index, cur, result):
        if rest == 0:
            result.append(cur[:])
            return
        for i in range(index, len(candidates)):
            if i != index and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] <= rest:
                cur.append(candidates[i])
                self.dfs(rest - candidates[i], candidates, i + 1, cur, result)
                cur.pop()

    def combinationSum2(self, candidates, target):
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
print(s.combinationSum2([10,1,2,7,6,1,5], 8))
print(s.combinationSum2([2,5,2,1,2], 5))
