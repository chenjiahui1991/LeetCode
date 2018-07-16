# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals + [newInterval], key = lambda x : x.start)
        result = []
        left = -float('inf')
        right = -float('inf')
        for i in range(len(intervals)):
            if intervals[i].start > right:
                if left != -float('inf'):
                    result.append(Interval(left, right))
                left = intervals[i].start
                right = intervals[i].end
            else:
                right = max(right, intervals[i].end)
        if right != -float('inf'):
            result.append(Interval(left, right))
        return result


s = Solution()
tmp = s.insert([Interval(1, 3), Interval(6, 9)], Interval(2, 5))
for val in tmp:
    print(val.start, val.end)
