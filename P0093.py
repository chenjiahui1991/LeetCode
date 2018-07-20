class Solution:
    def dfs(self, deep, str, subset, set):
        if len(str) > deep * 3 or len(str) < deep:
            return
        if deep == 0:
            set.append(subset[:])
        else:
            for i in range(min(3, len(str))):
                num = str[:i + 1]
                if (num[0] == '0' and i == 0) or (num[0] != '0' and 1 <= int(str[:i + 1]) <= 255):
                    if deep == 1:
                        subset += num
                    else:
                        subset += num + '.'
                    self.dfs(deep - 1, str[i + 1:], subset, set)
                    if deep == 1:
                        subset = subset[:-len(num)]
                    else:
                        subset = subset[:-len(num)-1]

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.dfs(4, s, "", result)
        return result

s = Solution()
print(s.restoreIpAddresses("010010"))
