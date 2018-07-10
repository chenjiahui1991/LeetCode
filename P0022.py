class Solution:
    result = []
    def dfs(self, left, middle, right, str):
        if left == 0 and middle == 0:
            self.result.append(str)
            return
        if left > 0:
            self.dfs(left - 1, middle + 1, right, str + '(')
        if middle > 0:
            self.dfs(left, middle - 1, right + 1, str + ')')


    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.dfs(n, 0, 0, '')
        return self.result


s = Solution()
print(s.generateParenthesis(2))

