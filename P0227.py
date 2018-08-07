class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        sgn = lambda x: 1 if x > 0 else -1 if x < 0 else 0
        def calcStack(stack, op, opset):
            while len(op) > 0 and op[-1] in opset:
                tmp = op.pop()
                b = stack.pop()
                a = stack.pop()
                if tmp == '+':
                    stack.append(int(a) + int(b))
                elif tmp == '-':
                    stack.append(int(a) - int(b))
                elif tmp == '*':
                    stack.append(int(a) * int(b))
                elif tmp == '/':
                    stack.append(abs(int(a)) // abs(int(b)) * sgn(int(a)) * sgn(int(b)))

        s = ''.join(s.split())
        op = []
        stack = []
        current = ''
        for ch in s:
            if '0' <= ch <= '9':
                current += ch
            if ch in ['+', '-']:
                stack.append(current)
                current = ''
                calcStack(stack, op, ['+', '-', '*', '/'])
                op.append(ch)
            if ch in ['*', '/']:
                stack.append(current)
                current = ''
                calcStack(stack, op, ['*', '/'])
                op.append(ch)
        if current != "": stack.append(current)
        calcStack(stack, op, ['+', '-', '*', '/'])
        return int(stack[0])



s = Solution()
print(s.calculate("3+2*2"))
print(s.calculate( " 3/2 "))
print(s.calculate(" 3+5 / 2 "))

