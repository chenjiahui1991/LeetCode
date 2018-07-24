class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        lowest = float('inf')
        for val in prices:
            result = max(val - lowest, result)
            lowest = min(lowest, val)
        return result

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([1,2,3,4,5]))
print(s.maxProfit([7,6,4,3,1]))
