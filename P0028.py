class Solution:
    def getNext(self,needle):
        next = [0] * len(needle)
        next[0] = -1
        k = -1
        for j in range(1, len(needle)):
            while k != -1 and needle[k + 1] != needle[j]:
                k = next[k]
            if needle[k + 1] == needle[j]:
                next[j] = k + 1
                k = k + 1
            else:
                next[j] = k
        return next

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        next = self.getNext(needle)
        i = 0
        j = -1
        while i < len(haystack) and j < len(needle) - 1:
            print(i, j)
            while j != -1 and haystack[i] != needle[j + 1]:
                j = next[j]
            if haystack[i] == needle[j + 1]:
                j = j + 1
            i = i + 1
        if j == len(needle) - 1:
            return i - j - 1
        else:
            return -1

s = Solution()
print(s.strStr("", ""))

