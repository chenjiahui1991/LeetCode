class Solution:
    def largestRectangleArea(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        left = [i for i in range(len(heights))]
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]: left[i] = left[stack.pop()]
            stack.append(i)
        right = [i for i in range(len(heights))]
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]: right[i] = right[stack.pop()]
            stack.append(i)
        return max([heights[i] * (right[i] - left[i] + 1) for i in range(len(heights))])

s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))
