class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        strList = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        valList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        mem = dict()
        for i, str in enumerate(strList):
            mem[str] = valList[i]
        result = 0
        skip = 0
        for i, ch in enumerate(s):
            if skip == 1:
                skip = 0
                continue
            if s[i : i + 2] in mem:
                result = result + mem[s[i : i + 2]]
                skip = 1
            else:
                result = result + mem[s[i]]
        return result



s = Solution()
print(s.romanToInt('III'))
print(s.romanToInt('IV'))
print(s.romanToInt('IX'))
print(s.romanToInt('LVIII'))
print(s.romanToInt('MCMXCIV'))


