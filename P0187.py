from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        mem = defaultdict(lambda :0)
        for i in range(len(s) - 9):
            mem[s[i : i + 10]] += 1
        result = []
        for key in mem:
            if mem[key] > 1: result.append(key)
        return result

s = Solution()
print(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
