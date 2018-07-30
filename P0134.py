class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        def feasible(gas, cost):
            tank = 0
            for i in range(len(gas)):
                tank = tank + gas[i] - cost[i]
                if tank < 0:
                    return False, i
            return True, 0

        i = 0
        while i < len(gas):
            ok, next = feasible(gas[i:] + gas[:i], cost[i:] + cost[:i])
            if ok: return i
            i = max(i + next, i + 1)
        return -1


s = Solution()
print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
print(s.canCompleteCircuit([2,3,4], [3,4,3]))
