class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        totalA = sum(A)
        totalB = sum(B)

        flag = set()
        for b in B:
            flag.add(b)
        delta = (totalB - totalA) // 2
        for a in A:
            if (a + delta) in flag:
                return [a, a + delta]
        return None



A = [1, 2, 5]
B = [2, 4]
s = Solution()
# for i in range(30):
#     print(s.superEggDrop(3, i), end=',')
# print()
print(s.fairCandySwap(A, B))
