class Solution:
    def dfs(self, deep, keys, mem, count, subset, set, n):
        if deep == n:
            set.append(subset[:])
        else:
            for i in range(count[mem[keys[deep]]] + 1):
                self.dfs(deep + 1, keys, mem, count, subset, set, n)
                subset.append(keys[deep])
            for i in range(count[mem[keys[deep]]] + 1):
                subset.pop()

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        mem = dict()
        count = []
        for val in nums:
            if val in mem:
                count[mem[val]] += 1
            else:
                count.append(1)
                mem[val] = len(count) - 1
        keys = [key for key in mem]
        result = []
        self.dfs(0, keys, mem, count, [], result, len(keys))
        return result




s = Solution()
print(s.subsetsWithDup([1, 2, 2]))

