class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = '1'
        for i in range(1, n):
            tmp = ''
            point = 0
            while point < len(result):
                count = 1
                while point < len(result) - 1 and result[point + 1] == result[point]:
                    count = count + 1
                    point = point + 1
                tmp = tmp + str(count) + result[point]
                point = point + 1
            result = tmp
        return result


s = Solution()
print(s.countAndSay(1))
