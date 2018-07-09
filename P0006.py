class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        strList = [''] * numRows
        point = 0
        step = 1
        for ch in s:
            strList[point] = strList[point] + ch
            point = point + step
            if point == numRows:
                point = numRows - 2
                step = -1
            elif point == -1:
                point = 1
                step = 1
        result = ''.join(strList)
        return result


s = Solution()
print(s.convert("PAYPALISHIRING", 3))
print(s.convert("PAYPALISHIRING", 4))

