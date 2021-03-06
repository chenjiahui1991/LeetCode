class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        while n > 1:
            if n & 1 == 1:
                return False
            n = n >> 1
        return True


s = Solution()
print(s.isPowerOfTwo(218))

