class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = int(0)
        for i in range(32):
            result = (result << 1) + (n & 1)
            n = n >> 1
        return result


s = Solution()
print(s.reverseBits(43261596))
