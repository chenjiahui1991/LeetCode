class Solution:
    mem = dict()

    def dfs(self, n):
        if n in self.mem:
            return self.mem[n]
        if n == 0:
            return 1
        result = 0
        for i in range(n):
            left = self.dfs(i)
            right = self.dfs(n - 1 - i)
            result += left * right
        self.mem[n] = result
        return result

    def numTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return 0
        return self.dfs(n)

s = Solution()
print(s.numTrees(19))
