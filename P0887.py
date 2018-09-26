class Solution:
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        N = N + 1
        f = dict()
        def dfs(K, N):
            if (K, N) in f: return f[(K, N)]
            if N <= 1:
                f[(K, N)] = 0
                return f[(K, N)]
            if K == 1:
                f[(K, N)] = max(0, N - 1)
                return f[(K, N)]
            lo, hi = 1, N - 1
            while lo + 1 < hi:
                mid = (lo + hi) >> 1
                left = dfs(K, mid)
                right = dfs(K - 1, N - mid)
                if left < right:
                    lo = mid
                elif left > right:
                    hi = mid
                else:
                    lo = hi = mid
            f[(K, N)] = 1 + min(max(dfs(K, x), dfs(K - 1, N - x)) for x in range(lo, hi + 1))
            return f[(K, N)]
        return dfs(K, N)


s = Solution()
# for i in range(30):
#     print(s.superEggDrop(3, i), end=',')
# print()
print(s.superEggDrop(1, 2))
print(s.superEggDrop(3, 25))
print(s.superEggDrop(2, 9))
print(s.superEggDrop(5, 14))
print(s.superEggDrop(4, 5000))
