class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        result = ""
        if numerator / denominator < 0: result = '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        result += str(numerator // denominator)
        if numerator % denominator == 0:
            return result
        result += "."
        fracpart = ''
        rest = numerator % denominator
        mem = dict()
        count = 0
        while rest not in mem and rest != 0:
            mem[rest] = count
            count += 1
            rest *= 10
            fracpart += str(rest // denominator)
            rest = rest % denominator
        if rest == 0: return result + fracpart
        fracpart = fracpart[: mem[rest]] + '(' + fracpart[mem[rest]:] + ')'
        return result + fracpart


s = Solution()
print(s.fractionToDecimal(1, 6))
print(s.fractionToDecimal(-2, 1))
print(s.fractionToDecimal(2, -3))
for i in range(8):
    print(s.fractionToDecimal(i, 7))
