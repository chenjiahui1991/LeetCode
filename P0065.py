class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if len(s) == 0:
            return False
        if not(s[0] == '+' or s[0] == '-' or s[0] == '.' or '0' <= s[0] <= '9'):
            return False
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        point = 0
        while point < len(s) and '0' <= s[point] <= '9':
            point += 1
        if point == len(s):
                return True
        if s[point] == '.':
            if point < len(s) - 1 and s[point + 1] == 'e':
                if not(point != 0 and '0' <= s[point - 1] <= '9'):
                    return False
            point = point + 1
            while point < len(s) and '0' <= s[point] <= '9':
                point += 1
        if point == len(s):
            if point == 1:
                return False
            else:
                return True
        if s[point] == 'e' and point != len(s) - 1:
            if point == 0:
                return False
            s = s[point + 1 :]
            if not(s[0] == '+' or s[0] == '-' or '0' <= s[0] <= '9'):
                return False
            if s[0] == '+' or s[0] == '-':
                s = s[1:]
            if len(s) == 0:
                return False
            point = 0
            while point < len(s) and '0' <= s[point] <= '9':
                point += 1
            if point == len(s):
                return True
            return False
        else:
            return False


s = Solution()
map = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(s.isNumber("-e58"))
