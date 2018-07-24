class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        result = [[1]]
        last = [1]
        for i in range(1, numRows):
            current = [1]
            for j in range(i - 1):
                current.append(last[j] + last[j + 1])
            current.append(1)
            result.append(current[:])
            last = current
        return result

s = Solution()
print(s.generate(33))
