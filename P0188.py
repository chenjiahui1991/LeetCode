class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        def maxValue(prices):
            result = 0
            for i in range(1, len(prices)):
                result += max([prices[i] - prices[i - 1], 0])
            return result
        if len(prices) < 2 or k == 0: return 0
        if k >= len(prices) // 2: return maxValue(prices)
        local = [[0 for _ in range(k + 1)] for _ in range(len(prices))]
        total = [[0 for _ in range(k + 1)] for _ in range(len(prices))]
        for i in range(1, k + 1):
            for j in range(1, len(prices)):
                local[j][i] = max(local[j - 1][i] + prices[j] - prices[j - 1], total[j - 1][i - 1] + max(prices[j] - prices[j - 1], 0))
                total[j][i] = max(total[j - 1][i], local[j][i])
        return total[-1][-1]

s = Solution()
print(s.maxProfit(100, [3,2,6,5,0,3]))
print(s.maxProfit(2, [2, 4, 1]))
