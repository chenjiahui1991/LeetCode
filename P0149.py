from collections import defaultdict
import math

# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) == 0: return 0
        weigth = defaultdict(lambda :0)
        for point in points:
            weigth[(point.x, point.y)] += 1
        points = list(weigth.keys())
        result = 0
        if len(points) == 1: return weigth[points[0]]
        for i in range(len(points)):
            mem = defaultdict(lambda :0)
            for j in range(i + 1, len(points)):
                if points[i][0] == points[j][0]:
                    mem['#'] += weigth[points[j]]
                else:
                    k = (float(points[i][1]) - float(points[j][1])) / (float(points[i][0]) - float(points[j][0]))
                    mem[k] += weigth[points[j]]
            if len(mem.values()) > 0:
                result = max(result, weigth[points[i]] + max(mem.values()))
        return result


s = Solution()
print(s.maxPoints([Point(1, 1), Point(3, 2), Point(5, 3), Point(4, 1), Point(2, 3), Point(1, 4)]))
print(s.maxPoints([Point(0, 0), Point(0, 0), Point(1, 1)]))
