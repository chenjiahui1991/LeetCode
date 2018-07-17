class Solution:
    def dfs(self, deep, cand, set, result):
        if deep == len(cand):
            result.append(set[:])
        else:
            for val in [True, False]:
                if val:
                    set.append(cand[deep])
                self.dfs(deep + 1, cand, set, result)
                if val:
                    set.pop()

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(0, nums, [], result)
        return result



s = Solution()
print(s.subsets([1,2,3]))
