class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        op = ['+', '-', '*', '/']
        for item in tokens:
            if item not in op:
                stack.append(int(item))
            else:
                b = stack.pop()
                a = stack.pop()
                if item == '+':
                    stack.append(a + b)
                elif item == '-':
                    stack.append(a - b)
                elif item == '*':
                    stack.append(a * b)
                else:
                    stack.append(abs(a) // abs(b) if a * b > 0 else -(abs(a) // abs(b)))
        return stack[0]


s = Solution()
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
print(s.evalRPN(["4", "13", "5", "/", "+"]))
print(s.evalRPN(["2", "1", "+", "3", "*"]))
