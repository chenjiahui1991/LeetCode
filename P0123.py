class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        n = len(prices)
        if n == 0: return 0
        left = [0 for _ in range(n)]
        lowest = float('inf')
        for i, val in enumerate(prices):
            result = max(val - lowest, result)
            left[i] = result
            lowest = min(lowest, val)

        result = 0
        right = [0 for _ in range(n)]
        highest = -float('inf')
        for i in range(n - 1, -1, -1):
            result = max(highest - prices[i], result)
            right[i] = result
            highest = max(highest, prices[i])

        result = max(left[-1], -right[0])
        for i in range(1, n - 1):
            result = max(result, left[i] + right[i + 1])
        return result

s = Solution()
print(s.maxProfit([3,3,5,0,0,3,1,4]))
print(s.maxProfit([1,2,3,4,5]))
print(s.maxProfit([7,6,4,3,1]))
