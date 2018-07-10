class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        if dividend < 0:
            sign = -1
            dividend = -dividend
        else:
            sign = 1
        if divisor < 0:
            sign = -sign
            divisor = -divisor
        result = 0
        list1 = [divisor]
        list2 = [1]
        attempt = divisor
        cum = 1

        while attempt + attempt < dividend:
            attempt = attempt + attempt
            cum = cum + cum
            list1.append(attempt)
            list2.append(cum)

        for i in range(len(list1) - 1, -1, -1):
            while dividend >= list1[i]:
                result = result + list2[i]
                dividend = dividend - list1[i]
        return result * sign

s = Solution()
print(s.divide(-7, 3))

