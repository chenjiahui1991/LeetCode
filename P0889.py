class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        step = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = [[r0, c0]]
        x = r0
        y = c0
        direction = 0
        count = 1
        base = 0
        while count < R * C:
            for i in range(base // 2 + 1):
                x = x + step[direction][0]
                y = y + step[direction][1]
                if 0 <= x < R and 0 <= y < C:
                    result.append([x, y])
                    count += 1
            base += 1
            direction = (direction + 1) % 4
        return result



s = Solution()
print(s.spiralMatrixIII(1, 4, 0, 0))
print(s.spiralMatrixIII(5, 6, 1, 4))
