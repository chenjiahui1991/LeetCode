class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = ''.join(s.split())
        op = []
        stack = []
        seperated = True
        for i, ch in enumerate(s):
            if '0' <= ch <= '9':
                if len(stack) > 0 and seperated == False:
                    stack[-1] = stack[-1] + ch
                else:
                    stack.append(ch)
                    seperated = False
                if ((i == len(s) - 1) or (i < len(s) - 1 and (not '0' <= s[i + 1] <= '9'))) and len(op) > 0 and op[-1] != '(':
                    tmp = op.pop()
                    b = stack.pop()
                    a = stack.pop()
                    if tmp == '+': stack.append(int(a) + int(b))
                    else: stack.append(int(a) - int(b))
            if ch in ['(', '+', '-']:
                op.append(ch)
                seperated = True
            if ch == ')':
                while len(op) > 0 and op[-1] != '(':
                    tmp = op.pop()
                    b = stack.pop()
                    a = stack.pop()
                    if tmp == '+': stack.append(int(a) + int(b))
                    else: stack.append(int(a) - int(b))
                op.pop()
                if len(op) > 0:
                    tmp = op.pop()
                    b = stack.pop()
                    a = stack.pop()
                    if tmp == '+': stack.append(int(a) + int(b))
                    else: stack.append(int(a) - int(b))
                seperated = True
        return int(stack[0])



s = Solution()
print(s.calculate("1 - (5)"))
print(s.calculate("1 - 11"))
print(s.calculate("1 + 1"))
print(s.calculate(" 2-1 + 2 "))
print(s.calculate("(1+(4+5+2)-3)+(6+8)"))

