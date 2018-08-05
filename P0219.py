from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lastPosition = defaultdict(lambda : -float('inf'))
        for i in range(len(nums)):
            if i - lastPosition[nums[i]] <= k:
                return True
            lastPosition[nums[i]] = i
        return False


s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1], 3))
print(s.containsNearbyDuplicate([1,0,1,1], 1))
print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))
