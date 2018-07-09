class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        left = 0
        right = len(height) - 1
        while left < right:
            current = min(height[left], height[right]) * (right - left)
            if current > result:
                result = current
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return result


s = Solution()
print(s.maxArea([1, 2, 4, 3]))


