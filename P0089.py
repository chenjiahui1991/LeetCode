import sys

class Solution:
    def dfs(self, deep, current, linked, visited, result):
        if deep == 0:
            return True
        count = [0 for i in range(len(linked[current]))]
        for i in range(len(linked[current])):
            for j in linked[linked[current][i]]:
                count[i] += 1 if visited[j] else 0
        tmp = sorted(enumerate(count), key=lambda x:x[1], reverse=True)
        for idx, _ in tmp:
            next = linked[current][idx]
            if visited[next] == False:
                visited[next] = True
                result.append(next)
                if self.dfs(deep - 1, next, linked, visited, result):
                    return True
                result.pop()
                visited[next] = False

    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        sys.setrecursionlimit(100000)
        total = 2 ** n
        mem = [2 ** i for i in range(n)]
        linked = [[] for _ in range(total)]
        for i in range(total):
            for j in range(i + 1, total):
                if i ^ j in mem:
                    linked[i].append(j)
                    linked[j].append(i)
        visited = [True] + [False for _ in range(total - 1)]
        result = [0]
        self.dfs(2 ** n - 1, 0, linked, visited, result)
        return result



s = Solution()
print(s.grayCode(10))

