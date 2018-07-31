class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        f = [[float('inf') for _ in range(n)] for _ in range(m)]
        f[-1][-1] = max(1, 1 - dungeon[-1][-1])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i != m - 1: f[i][j] = min(f[i][j], max(1, f[i + 1][j] - dungeon[i][j]))
                if j != n - 1: f[i][j] = min(f[i][j], max(1, f[i][j + 1] - dungeon[i][j]))
        return f[0][0]

board = [[-2,  -3,  3],
         [-5, -10,  1],
         [10,  30, -5]]
s = Solution()
print(s.calculateMinimumHP(board))
