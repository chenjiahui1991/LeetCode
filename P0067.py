class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ''
        point1 = len(a) - 1
        point2 = len(b) - 1
        carry = 0
        while point1 >= 0 or point2 >= 0:
            if point1 >= 0:
                carry += ord(a[point1]) - ord('0')
            if point2 >= 0:
                carry += ord(b[point2]) - ord('0')
            result = chr(carry % 2 + ord('0')) + result
            carry = carry // 2
            point1 -= 1
            point2 -= 1
        if carry == 1:
            result = '1' + result
        return result


s = Solution()
print(s.addBinary("0", "0"))
