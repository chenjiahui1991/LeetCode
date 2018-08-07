class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a, ca = 0, 0
        b, cb = 0, 0
        for num in nums:
            if ca > 0 and num == a:
                ca += 1
            elif cb > 0 and num == b:
                cb += 1
            elif ca == 0:
                a = num
                ca = 1
            elif cb == 0:
                b = num
                cb = 1
            else:
                ca -= 1
                cb -= 1
        ca, cb = 0, 0
        for num in nums:
            if num == a: ca += 1
            if num == b: cb += 1
        result = []
        if ca > len(nums) // 3: result.append(a)
        if cb > len(nums) // 3 and a != b: result.append(b)
        return result

s = Solution()
print(s.majorityElement([3,2,3]))
print(s.majorityElement([1,1,1,3,3,2,2,2]))
print(s.majorityElement([0, 0, 0]))

