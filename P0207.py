from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses == 0: return True
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
                    for course in next[i]: inDegree[course] -= 1
            tmp2 = sum(inDegree)
            if tmp1 == tmp2: return False
        return True


s = Solution()
print(s.canFinish(2, [[1,0],[0,1]]))
print(s.canFinish(2, [[1,0]]))
