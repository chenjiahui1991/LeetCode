class Solution:
    def findOptimal(self, piles, start, end):
        if (start, end) in self.mem:
            return self.mem[(start, end)]
        if start == end:
            self.mem[(start, end)] = (piles[start], 0)
            return (piles[start], 0)
        a1, b1 = self.findOptimal(piles, start + 1, end)
        a2, b2 = self.findOptimal(piles, start, end - 1)
        if piles[start] + b1 > piles[end] + b2:
            self.mem[(start, end)] = (piles[start] + b1, a1)
            return (piles[start] + b1, a1)
        else:
            self.mem[(start, end)] = (piles[end] + b2, a2)
            return (piles[end] + b2, a2)

    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        self.mem = dict()
        a, b = self.findOptimal(piles, 0, len(piles) - 1)
        return a > b

s = Solution()
print(s.stoneGame([5,3,4,5]))

