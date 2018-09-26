class Solution:
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        def getNumber(S, K):
            total = 0
            for i, ch in enumerate(S):
                if 'a' <= ch <= 'z':
                    total = total + 1
                else:
                    total = total * int(ch)
                if total >= K:
                    if 'a' <= ch <= 'z':
                        return ch
                    else:
                        lastLength = total // int(ch)
                        K = K % lastLength
                        if K == 0: K = lastLength
                        return getNumber(S[: i], K)
        return getNumber(S, K)

s = Solution()
print(s.decodeAtIndex("leet2code3", 10))
print(s.decodeAtIndex("ha22", 5))
print(s.decodeAtIndex("a2345678999999999999999", 10))

