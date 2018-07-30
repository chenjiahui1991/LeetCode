class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        ratings.append(ratings[-1])
        ratings = [ratings[0]] + ratings
        result = 0
        for i in range(1, len(ratings) - 1):
            if ratings[i] == ratings[i - 1]: current = 1
            elif ratings[i] > ratings[i - 1]: current += 1
            else: current -= 1
            result += current
            if ratings[i] >= ratings[i - 1]:
                left = i
            else:
                if ratings[i] <= ratings[i + 1]:
                    if current < 1:
                        result += (1 - current) * (i - left + 1)
                    else:
                        result += (1 - current) * (i - left)
                    current = 1
        return result





s = Solution()
print(s.candy([1,2,87,87,87,2,1]))
print(s.candy([1,2,2]))
