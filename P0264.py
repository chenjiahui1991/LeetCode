import heapq

class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        flag = set()
        flag.add(1)
        h = [1]
        for i in range(n - 1):
            minValue = heapq.heappop(h)
            if minValue * 2 not in flag:
                heapq.heappush(h, minValue * 2)
                flag.add(minValue * 2)
            if minValue * 3 not in flag:
                heapq.heappush(h, minValue * 3)
                flag.add(minValue * 3)
            if minValue * 5 not in flag:
                heapq.heappush(h, minValue * 5)
                flag.add(minValue * 5)
        return heapq.heappop(h)


s = Solution()
print(s.nthUglyNumber(12))
