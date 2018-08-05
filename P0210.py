from collections import defaultdict

class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        result = []
        if numCourses == 0: return []
        inDegree = [0 for _ in range(numCourses)]
        learnt = [False for _ in range(numCourses)]
        next = defaultdict(list)
        for tail, head in prerequisites:
            inDegree[tail] += 1
            next[head].append(tail)
        while sum(inDegree) != 0:
            tmp1 = sum(inDegree)
            for i in range(numCourses):
                if learnt[i] == False and inDegree[i] == 0:
                    learnt[i] = True
                    result.append(i)
                    for course in next[i]: inDegree[course] -= 1
            tmp2 = sum(inDegree)
            if tmp1 == tmp2: return []
        for i in range(numCourses):
            if learnt[i] == False: result.append(i)
        return result


s = Solution()
print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(s.findOrder(2, [[1,0]]))
