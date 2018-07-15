class Solution:
    n = 0
    result = 0

    def dfs(self, deep, col, left, right):
        if deep == 0:
            self.result += 1
            return
        for i in range(self.n):
            if not i in col and not deep + i in right and not deep - i in left:
                col.append(i)
                right.append(deep + i)
                left.append(deep - i)
                self.dfs(deep - 1, col, left, right)
                left.pop()
                right.pop()
                col.pop()


    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        result = []
        self.dfs(n, [], [], [])
        return self.result



s = Solution()
print(s.totalNQueens(4))
