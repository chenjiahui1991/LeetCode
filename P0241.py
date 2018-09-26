class Solution:
    _OPERATIONS = {
        '+' : lambda x, y : x + y,
        '-' : lambda x, y : x - y,
        '*' : lambda x, y : x * y
    }

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        mem = dict()

        def dfs(start, end):
            if (start, end) in mem: return mem[(start, end)]
            result = []
            for i in range(start, end):
                op = self._OPERATIONS.get(input[i])
                if op:
                    for x in dfs(start, i):
                        for y in dfs(i + 1, end):
                            result.append(op(x, y))
            mem[(start, end)] = result if result else [int(input[start : end])]
            return mem[(start, end)]

        return dfs(0, len(input))


s = Solution()
print(s.diffWaysToCompute("2*3-4*5"))
