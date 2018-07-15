class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a = []
        b = []
        for i in range(len(num1) - 1, -1, -1):
            a.append(ord(num1[i]) - ord('0'))
        for i in range(len(num2) - 1, -1, -1):
            b.append(ord(num2[i]) - ord('0'))
        c = [0] * 300
        for i in range(0, len(a)):
            for j in range(0, len(b)):
                c[i + j] += a[i] * b[j]
        for i in range(0, len(c) - 2):
            c[i + 1] += c[i] // 10
            c[i] = c[i] % 10
        first = 0
        for i in range(len(c) - 1, -1, -1):
            if c[i] > 0:
                first = i
                break
        result = ''
        for i in range(first, -1, -1):
            result += chr(c[i] + ord('0'))
        return result

s = Solution()
print(s.multiply('123', '456'))
