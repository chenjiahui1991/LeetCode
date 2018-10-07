class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = 0
        for num in nums:
            tmp = tmp ^ num
        flag = tmp & (-tmp + 1)
        tmp1 = 0
        tmp2 = 0
        for num in nums:
            if flag & num == 0:
                tmp1 ^= num
            else:
                tmp2 ^= num
        return [tmp1, tmp2]



s = Solution()
print(s.singleNumber([1,2,1,3,2,5]))
