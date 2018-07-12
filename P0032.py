class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        stack = [-1]
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                if len(stack) != 1:
                    tmp = stack.pop()
                    if i - stack[-1] > result:
                        result = i - stack[-1]
                else:
                    stack[0] = i
        return result




s = Solution()
print(s.longestValidParentheses(")()())"))
