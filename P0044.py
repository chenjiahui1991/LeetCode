class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == '':
            if s == '':
                return True
            else:
                return False
        flag = [False] * (len(s) + 1)
        flag[0] = True
        for ch in p:
            cur = [False] * (len(s) + 1)
            if ch == '*':
                if flag[0] == True:
                    cur[0] = True
                for i in range(1, len(flag)):
                    if flag[i] == True or cur[i - 1] == True:
                        cur[i] = True
            else:
                for i in range(0, len(flag) - 1):
                    if flag[i] == True and (s[i] == ch or ch == '?'):
                        cur[i + 1] = True
            flag = cur
        return flag[-1]

s = Solution()
print(s.isMatch('', '*'))
print(s.isMatch('', '***a'))
print(s.isMatch('', ''))
print(s.isMatch("", "****"))
