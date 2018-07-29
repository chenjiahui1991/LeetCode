class Solution:
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        f = [dict() for _ in range(G + 1)]
        f[G][0] = 1
        for i in range(len(group)):
            for weight in range(group[i], G + 1):
                for total in f[weight]:
                    newWeight = weight - group[i]
                    newProfit = min(total + profit[i], P)
                    if newProfit in f[newWeight]:
                        f[newWeight][newProfit] = (f[newWeight][newProfit] + f[weight][total]) % (10 ** 9 + 7)
                    else:
                        f[newWeight][newProfit] = f[weight][total] % (10 ** 9 + 7)
        result = 0
        for i in range(G + 1):
            if P in f[i]:
                result =  (result + f[i][P]) % (10 ** 9 + 7)
        return result


s = Solution()
print(s.profitableSchemes(5, 3, [2, 2], [2, 3]))
print(s.profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8]))

