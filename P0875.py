import math

class Solution:
    def calcTime(self, piles, k):
        time = 0
        for val in piles:
            time += math.ceil(val * 1.0 / k)
        return time

    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        sum = 0
        for val in piles:
            sum += val
        left = math.ceil(sum * 1.0 / H)
        right = max(piles)
        while left < right:
            if self.calcTime(piles, left) <= H: return left
            mid = (left + right) // 2
            time = self.calcTime(piles, mid)
            if time > H:
                left = mid + 1
            else:
                right = mid
        return left

s = Solution()
print(s.minEatingSpeed([30,11,23,4,20], 6))
print(s.minEatingSpeed([30,11,23,4,20], 5))
print(s.minEatingSpeed([3,6,7,11], 8))
# 4
