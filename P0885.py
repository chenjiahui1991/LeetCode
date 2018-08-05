class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        left, right = 0, len(people) - 1
        result = 0
        while left < right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
                result += 1
            else:
                right -= 1
                result += 1
        if left == right: result += 1
        return result



s = Solution()
print(s.numRescueBoats([1,2], 3))
print(s.numRescueBoats([3,2,2,1],3))
print(s.numRescueBoats([3, 4, 3, 4], 5))

