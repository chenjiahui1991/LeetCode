class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        result = 0
        tmp = sorted(enumerate(height), key=lambda x:x[1], reverse=True)
        idx = [x[0] for x in tmp]
        left = right = idx[0]
        for i in range(1, len(height)):
            if idx[i] < left:
                for j in range(idx[i] + 1, left):
                    result += height[idx[i]] - height[j]
                left = idx[i]
            elif idx[i] > right:
                for j in range(right + 1, idx[i]):
                    result += height[idx[i]] - height[j]
                right = idx[i]
        return result

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
