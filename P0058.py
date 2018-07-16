class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        result = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                return result
            else:
                result += 1
        return result

s = Solution()
print(s.lengthOfLastWord("Hello World"))
