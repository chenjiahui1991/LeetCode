class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        n = len(prices)
        prices.append(-float('inf'))
        lowest = float('inf')
        for i in range(n):
            if prices[i] >= prices[i + 1]:
                result += max(0, prices[i] - lowest)
                lowest = float('inf')
            else:
                lowest = min(lowest, prices[i])
        return result

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([1,2,3,4,5]))
print(s.maxProfit([7,6,4,3,1]))
