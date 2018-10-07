class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0: return 0
        citations.sort()
        if citations[0] >= len(citations): return len(citations)
        if citations[-1] == 0: return 0
        for i in range(len(citations) - 1):
            h = len(citations) - i - 1
            if (citations[i + 1] >= h) and (citations[i] <= h):
                return h



s = Solution()
print(s.hIndex([3,0,6,1,5]))
print(s.hIndex([]))
