class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        flag = [[True for col in range(n)] for row in range(n)]
        for i in range(n):
            for j in range(n):
                if flag[i][j]:
                    tmp = matrix[i][j]
                    matrix[i][j] = matrix[n - j - 1][i]
                    matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                    matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                    matrix[j][n - i - 1] = tmp
                    flag[i][j] = False
                    flag[n - j - 1][i] = False
                    flag[n - i - 1][n - j - 1] = False
                    flag[j][n - i - 1] = False
                # print(matrix)


s = Solution()
img = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
s.rotate(img)
print(img)
