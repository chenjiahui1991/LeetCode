from heapq import *
class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(buildings) == 0: return []
        coords = set()
        for building in buildings:
            coords.add(building[0])
            coords.add(building[1])
        coords = list(coords)
        coords.sort()
        point = 0
        heap = [[0, coords[0], coords[-1] + 1]]
        result = []
        heapify(heap)
        last = -1
        for coord in coords:
            while point < len(buildings) and buildings[point][0] == coord:
                heappush(heap, [-buildings[point][2], buildings[point][0], buildings[point][1]])
                point += 1
            while heap[0][2] <= coord:
                heappop(heap)
            if -heap[0][0] != last:
                result.append([coord, -heap[0][0]])
                last = -heap[0][0]
        return result


s = Solution()
print(s.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
