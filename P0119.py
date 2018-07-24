class Solution:
    def getRow(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        numRows += 1
        last = [1]
        for i in range(1, numRows):
            current = [1]
            for j in range(i - 1):
                current.append(last[j] + last[j + 1])
            current.append(1)
            last = current
        return last

s = Solution()
print(s.getRow(3))
