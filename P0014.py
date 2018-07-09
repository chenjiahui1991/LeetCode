class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        result = strs[0]
        for i in range(1, len(strs)):
            result = self.getLongest(result, strs[i])
        return result

    def getLongest(self, str1, str2):
        result = '';
        if len(str1) > len(str2):
            tmp = str1
            str1 = str2
            str2 = tmp
        for i, ch in enumerate(str1):
            if ch == str2[i]:
                result = result + ch
            else:
                return result
        return result



s = Solution()
print(s.longestCommonPrefix(['flower','flow','flight']))


