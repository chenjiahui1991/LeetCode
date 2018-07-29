class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        mem = dict()
        for num in nums:
            mem[num] = 1

        for num in mem:
            if mem[num] == 1:
                left = num
                right = num
                mem[num] = -1
                i = num - 1
                while i in mem and mem[i] == 1:
                    mem[i] = -1
                    left -= 1
                    i -= 1
                i = num + 1
                while i in mem and mem[i] == 1:
                    mem[i] = -1
                    right += 1
                    i += 1
                if right - left + 1 > result: result = right - left + 1
        return result

s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
