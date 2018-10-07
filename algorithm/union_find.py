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

# s = unionFind(6)
# s.union(1, 2)
# s.union(3, 5)
# s.union(3, 1)
# for i in range(1, 6):
#     print(s.get_father(i))
# print(s.is_same_set(2, 5))
# print(s.is_same_set(4, 5))
