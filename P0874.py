# Definition for a binary tree node.
from collections import defaultdict

class Solution:
    def getGap(self, nums, val):
        nums = sorted(nums)
        tmp = [-float('inf')] + nums + [float('inf')]
        left = 0
        right = len(tmp)
        while True:
            if left + 1 == right: return tmp[left], tmp[right]
            mid = (left + right) // 2
            if tmp[mid] < val:
                left = mid
            else:
                right = mid

    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows = defaultdict(list)
        cols = defaultdict(list)
        for val in obstacles:
            cols[val[0]].append(val[1])
            rows[val[1]].append(val[0])
        position = [0, 0]
        step = 0
        result = 0
        for val in commands:
            if val == -2:
                step = (step + 3) % 4
            elif val == -1:
                step = (step + 1) % 4
            else:
                if directions[step][0] == 0:
                    minVal, maxVal = self.getGap(cols[position[0]], position[1])
                    if directions[step][1] > 0:
                        position[1] = min(maxVal - 1, position[1] + val)
                    else:
                        position[1] = max(minVal + 1, position[1] - val)
                else:
                    minVal, maxVal = self.getGap(rows[position[1]], position[0])
                    if directions[step][0] > 0:
                        position[0] = min(maxVal - 1, position[0] + val)
                    else:
                        position[0] = max(minVal + 1, position[0] - val)
            result = max(position[0] ** 2 + position[1] ** 2, result)
        return result

s = Solution()
print(s.robotSim([7,-2,-2,7,5], [[-3,2],[-2,1],[0,1],[-2,4],[-1,0],[-2,-3],[0,-3],[4,4],[-3,3],[2,2]]))
# 4
