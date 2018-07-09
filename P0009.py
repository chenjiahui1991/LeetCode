class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        result = 0
        origin = x
        while x > 0:
            result = result * 10 + x % 10
            x = x // 10
        if result == origin:
            return True
        else:
            return False

s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
print(s.isPalindrome(0))


