class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        strList = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        last = [ch for ch in strList[ord(digits[0]) - ord('0')]]
        for ch in digits[1:]:
            now = []
            for newCh in strList[ord(ch) - ord('0')]:
                now = now + [str + newCh for str in last]
            last = now
        return last

s = Solution()
print(s.letterCombinations(''))


