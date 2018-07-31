class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        words = s.split()
        words = reversed(words)
        return " ".join(words)


s = Solution()
print(s.reverseWords("the sky is blue"))
