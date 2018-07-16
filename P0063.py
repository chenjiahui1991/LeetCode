class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        f = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if i == 0 and j == 0:
                        f[i][j] = 1
                    if i > 0 and obstacleGrid[i - 1][j] == 0:
                        f[i][j] += f[i - 1][j]
                    if j > 0 and obstacleGrid[i][j - 1] == 0:
                        f[i][j] += f[i][j - 1]
        return f[m - 1][n - 1]

s = Solution()
map = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
print(s.uniquePathsWithObstacles(map))
