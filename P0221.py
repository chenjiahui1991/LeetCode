class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        result = 0
        for i in range(n):
            dp[0][i] = int(matrix[0][i])
            result = max(result, dp[0][i])
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            result = max(result, dp[i][0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    matrix[i][j] = min(int(matrix[i - 1][j - 1]), int(matrix[i - 1][j]), int(matrix[i][j - 1])) + 1
                    result = max(result, matrix[i][j])
        return result * result


matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
s = Solution()
print(s.maximalSquare(matrix))

