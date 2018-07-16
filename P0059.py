class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        step = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        x = 0
        y = 0
        direction = 0
        for i in range(m * n):
            matrix[x][y] = i + 1
            visited[x][y] = True
            while i != m * n - 1 and not (0 <= x + step[direction][0] < m and 0 <= y + step[direction][1] < n and visited[x + step[direction][0]][y + step[direction][1]] == False):
                direction = (direction + 1) % 4
            x = x + step[direction][0]
            y = y + step[direction][1]
        return matrix



s = Solution()
print(s.generateMatrix(3))
