class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mem = set()
        for num in nums:
            if num in mem: return True
            mem.add(num)
        return False



s = Solution()
print(s.containsDuplicate([1,2,3,4]))
