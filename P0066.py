class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        for i in range(len(digits) - 1, 0, -1):
            digits[i - 1] += digits[i] // 10
            digits[i] = digits[i] % 10
        if digits[0] == 10:
            digits[0] = 0
            digits = [1] + digits
        return digits


s = Solution()
print(s.plusOne([9, 9, 9]))
