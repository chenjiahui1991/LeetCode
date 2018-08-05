class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def get_next(substr):
            next = [0] * len(substr)
            next[0] = -1
            k = -1
            for j in range(1, len(substr)):
                while k != -1 and substr[k + 1] != substr[j]:
                    k = next[k]
                if substr[k + 1] == substr[j]:
                    next[j] = k + 1
                    k = k + 1
                else:
                    next[j] = k
            return next


        def kmp(str, substr):
            result = []
            if substr == '':
                return result
            next = get_next(substr)
            i = 0
            j = -1
            while i < len(str):
                while j != -1 and str[i] != substr[j + 1]:
                    j = next[j]
                if str[i] == substr[j + 1]:
                    j = j + 1
                i = i + 1
            return j

        if len(s) == 0: return ""
        rs = s[::-1]
        return rs[:len(s) - kmp(rs, s) - 1] + s

s = Solution()
print(s.shortestPalindrome("aacecaaa"))
print(s.shortestPalindrome("abcd"))
print(s.shortestPalindrome("aa"))
