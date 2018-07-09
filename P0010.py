class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == p == '':
            return True
        lastF = [0] * (len(s) + 1)
        lastF[0] = 1
        nowF = None
        for i, ch in enumerate(p):
            if i != len(p) - 1 and p[i + 1] == '*':
                nowF = [0] * (len(s) + 1)
                if lastF[0] == 1:
                    nowF[0] = 1
                for j, val in enumerate(lastF[: -1]):
                    if (nowF[j] and (p[i] == s[j] or p[i] == '.')) or lastF[j + 1]:
                        nowF[j + 1] = 1
            elif p[i] == '*':
                continue
            else:
                nowF = [0] * (len(s) + 1)
                for j, val in enumerate(lastF[: -1]):
                    if lastF[j] and (p[i] == s[j] or p[i] == '.'):
                        nowF[j + 1] = 1
            lastF = nowF
            # print(i, ':', nowF)
        if nowF != None and nowF[-1] == 1:
            return True
        else:
            return False

s = Solution()
print(s.isMatch('aaa', 'ab*ac*a'))


