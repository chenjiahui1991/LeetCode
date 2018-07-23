class Solution:
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mem = set(A)
        n = len(A)
        if n <= 2: return 0
        result = 2
        for i in range(n):
            for j in range(i + 1, n):
                a, b = A[i], A[j]
                if b - a < a and b - a in mem: continue
                count = 2
                while a + b in mem:
                    count += 1
                    a, b = b, a + b
                result = max(count, result)
        return result if result > 2 else 0


s = Solution()
print(s.lenLongestFibSubseq([2,5,6,7,8,10,12,17,24,41,65]))
print(s.lenLongestFibSubseq([1,3,7,11,12,14,18]))


# 4
