class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        left = max(A, E)
        right = min(C, G)
        top = min(D, H)
        bottom = max(B, F)
        s1 = (C - A) * (D - B)
        s2 = (G - E) * (H - F)
        return s1 + s2 - max(right - left, 0) * max(top - bottom, 0)


s = Solution()
print(s.computeArea(A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2))

