class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        col = 1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        col = 0
                    else:
                        matrix[0][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(1, n):
                matrix[0][j] = 0
        if col == 0:
            for i in range(m):
                matrix[i][0] = 0


matrix = [[1],[0]]
s = Solution()
s.setZeroes(matrix)
print(matrix)
