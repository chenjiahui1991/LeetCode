class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        str1 = [ch for ch in s if 'a' <= ch <= 'z' or '0' <= ch <= '9']
        str2 = str1[:]
        str2.reverse()
        return str1 == str2


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome("0P"))
