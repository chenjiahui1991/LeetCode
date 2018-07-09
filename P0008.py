class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip()
        result = 0
        sign = 1
        min_val = -2 ** 31
        max_val = 2 ** 31 - 1
        for i, ch in enumerate(str):
            if i == 0 and ch == '-':
                sign = -1
            elif i == 0 and ch == '+':
                continue
            elif '0' <= ch <= '9':
                result = result * 10 + ord(ch) - ord('0')
            else:
                break
        result = sign * result
        if result > max_val:
            return max_val
        elif result < min_val:
            return min_val
        else:
            return result

s = Solution()
print(s.myAtoi('   \t-42'))
print(s.myAtoi('-91283472332'))
print(s.myAtoi('4193 with words'))
print(s.myAtoi('words and 987'))
print(s.myAtoi(''))
print(s.myAtoi('+2'))

