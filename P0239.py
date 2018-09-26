from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        line = deque()
        for i in range(len(nums)):
            if (line) and (line[0] == i - k):
                line.popleft()
            while (line) and (nums[i] >= nums[line[-1]]): line.pop()
            line.append(i)
            result.append(nums[line[0]])
        return result[k - 1:]


s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
