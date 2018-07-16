class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numList = [i for i in range(1, n + 1)]
        base = 1
        now = 1
        result = ""
        for i in range(1, n + 1):
            if base * i >= k:
                break
            base = base * i
            now = i
        for i in range(now + 2, n + 1):
            result += str(numList[0])
            numList.pop(0)
        for i in range(now, 0, -1):
            tmp = (k - 1) // base
            result = result + str(numList[tmp])
            numList.pop(tmp)
            k %= base
            base //= i
        if len(numList) > 0:
            return result + str(numList[0])
        else:
            return result




s = Solution()
for i in range(6):
    print(s.getPermutation(3, i + 1))
