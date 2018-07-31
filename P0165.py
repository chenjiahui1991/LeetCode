class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        words1 = version1.split(".")
        words2 = version2.split(".")
        if len(words1) < len(words2):
            for i in range(len(words2) - len(words1)):
                words1.append('0')
        else:
            for i in range(len(words1) - len(words2)):
                words2.append('0')
        for i in range(len(words1)):
            if int(words1[i]) > int(words2[i]):
                return 1
            if int(words1[i]) < int(words2[i]):
                return -1
        return 0

s = Solution()
print(s.compareVersion("0.1", "1.1"))
print(s.compareVersion("1.0.1", "1"))
print(s.compareVersion("7.5.2.4", "7.5.3"))
