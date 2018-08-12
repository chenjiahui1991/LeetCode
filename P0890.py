from collections import defaultdict

class Solution:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        next = defaultdict(list)
        for i, j in dislikes:
            next[i].append(j)
            next[j].append(i)
        color = [0 for _ in range(N + 1)]
        for i in range(1, N + 1):
            if color[i] == 0:
                line = [i]
                color[i] = 1
                point = 0
                while point < len(line):
                    now = line[point]
                    for j in next[now]:
                        if color[j] != 0 and color[j] == color[now]: return False
                        if color[j] == 0:
                            color[j] = 3 - color[now]
                            line.append(j)
                    point += 1
        return True



s = Solution()
print(s.possibleBipartition(4, []))
print(s.possibleBipartition(3, [[1,2],[1,3],[2,3]]))
print(s.possibleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]]))
