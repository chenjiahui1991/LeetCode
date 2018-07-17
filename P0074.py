class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        x = m - 1
        y = 0
        while x >= 0 and y < n:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                x -= 1
            else:
                y += 1
        return False


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
s = Solution()
print(s.searchMatrix(matrix, 16))
