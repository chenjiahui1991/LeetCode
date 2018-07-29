class Solution:
    def getCommon(self, a, b):
        oria, orib = a, b
        if a < b:
            a, b = b, a
        while b != 0:
            a, b = b, a % b
        return oria // a * orib

    def nthMagicalNumber(self, n, a, b):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        common = self.getCommon(a, b)
        round_ = common / a + common / b - 1
        tmp = n // round_
        if n % round_ == 0:
            return int((common % (10 ** 9 + 7) * tmp) % (10 ** 9 + 7))
        result = (common % (10 ** 9 + 7) * tmp) % (10 ** 9 + 7)
        rest = n % round_
        left, right = 0, rest
        while left <= right:
            mid = (left + right) // 2
            na, nb = mid, rest - mid
            if (na + 1) * a > nb * b and na * a < (nb + 1) * b:
                return int((result + max(na * a, nb * b)) % (10 ** 9 + 7))
            if (na + 1) * a < nb * b:
                left = mid + 1
            else:
                right = mid - 1


s = Solution()
print(s.nthMagicalNumber(1, 2, 3))
print(s.nthMagicalNumber(4, 2, 3))
print(s.nthMagicalNumber(5, 2, 4))
print(s.nthMagicalNumber(3, 6, 4))
