class unionFind():
    def __init__(self, n):
        self.father = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def get_father(self, i):
        if self.father[i] == i:
            return i
        self.father[i] = self.get_father(self.father[i])
        return self.father[i]

    def union(self, i, j):
        father_i = self.get_father(i)
        father_j = self.get_father(j)
        if father_i == father_j:
            return
        if self.size[father_i] > self.size[father_j]:
            self.father[father_j] = father_i
            self.size[father_i] = self.size[father_i] + self.size[father_j]
        else:
            self.father[father_i] = father_j
            self.size[father_j] = self.size[father_i] + self.size[father_j]

    def is_same_set(self, i, j):
        return self.get_father(i) == self.get_father(j)

class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        if n == 0: return 0
        u = unionFind(n)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if M[i][j]: u.union(i, j)
        mem = set()
        result = 0
        for i in range(n):
            father = u.get_father(i)
            if father not in mem:
                result += 1
                mem.add(father)
        return result

# M = [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
M = [[1,1,0],
 [1,1,1],
 [0,1,1]]
s = Solution()
print(s.findCircleNum(M))
