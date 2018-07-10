class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = ['(', '[', '{']
        right = [')', ']', '}']
        for ch in s:
            if ch in left:
                stack.append(ch)
            else:
                if len(stack) == 0 or left.index(stack.pop()) != right.index(ch):
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([)]"))
print(s.isValid("{[]}"))

