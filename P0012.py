class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        strList = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        valList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ''
        for i, val in enumerate(valList):
            while num >= val:
                result = result + strList[i]
                num = num - val
        return result



s = Solution()
print(s.intToRoman(3))
print(s.intToRoman(4))
print(s.intToRoman(9))
print(s.intToRoman(58))
print(s.intToRoman(1994))


