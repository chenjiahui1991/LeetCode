class Solution:
    def calcMaximalValue(self, heights):
        n = len(heights)
        left = [i for i in range(n)]
        right = [i for i in range(n)]
        stack = []
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]: left[i] = left[stack.pop()]
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]: right[i] = right[stack.pop()]
            stack.append(i)
        return max([heights[i] * (right[i] - left[i] + 1) for i in range(n)])

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        result = 0
        m = len(matrix)
        if m == 0 : return 0
        n = len(matrix[0])
        if n == 0 : return 0
        heights = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if heights[j] > 0:
                    heights[j] -= 1
                else:
                    now = i
                    while now < m and matrix[now][j] == '1':
                        heights[j] += 1
                        now += 1
            value = self.calcMaximalValue(heights)
            if value > result:
                result = value
        return result

s = Solution()
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
print(s.maximalRectangle(matrix))
