class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        result = 0
        col = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0: result += 1
                col[j].append(grid[i][j])
        for i in range(n):
            result += max(grid[i]) + max(col[i])
        return result


s = Solution()
print(s.projectionArea([[0]]))
print(s.projectionArea([[0,0],[0,1]]))
print(s.projectionArea([[2]]))
print(s.projectionArea([[1,2],[3,4]]))
print(s.projectionArea([[1,0],[0,2]]))
print(s.projectionArea([[1,1,1],[1,0,1],[1,1,1]]))
print(s.projectionArea([[2,2,2],[2,1,2],[2,2,2]]))
