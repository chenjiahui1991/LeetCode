class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        if n == 0: return 0
        for i in range(1, n):
            for j in range(i + 1):
                if j == 0: triangle[i][j] += triangle[i - 1][j]
                elif j == i: triangle[i][j] += triangle[i - 1][j - 1]
                else: triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
        return min(triangle[-1])

triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
s = Solution()
print(s.minimumTotal(triangle))
