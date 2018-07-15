class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        step = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        x = 0
        y = 0
        direction = 0
        for i in range(m * n):
            result.append(matrix[x][y])
            visited[x][y] = True
            while i != m * n - 1 and not (0 <= x + step[direction][0] < m and 0 <= y + step[direction][1] < n and visited[x + step[direction][0]][y + step[direction][1]] == False):
                direction = (direction + 1) % 4
            x = x + step[direction][0]
            y = y + step[direction][1]
        return result



s = Solution()
matrix = [
  [3],
  [2]
]
print(s.spiralOrder(matrix))
