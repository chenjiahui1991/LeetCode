class Solution:
    def reachableNodes(self, edges, M, N):
        """
        :type edges: List[List[int]]
        :type M: int
        :type N: int
        :rtype: int
        """
        next = [[] for _ in range(N)]
        for i, j, l in edges:
            next[i].append([j, l + 1])
            next[j].append([i, l + 1])
        f = [float('inf') for _ in range(N)]
        f[0] = 0
        # visited = [False for _ in range(N)]
        toGo = [0]
        inLine = [False for _ in range(N)]
        inLine[0] = True
        while len(toGo) > 0:
            selected = toGo[0]
            selected_index = 0
            for i in range(1, len(toGo)):
                if f[toGo[i]] < f[selected]:
                    selected = toGo[i]
                    selected_index = i
            inLine[selected_index] = False
            # visited[selected_index] = True
            if f[selected] > M: break
            toGo.pop(selected_index)
            for j, l in next[selected]:
                if f[selected] + l < f[j]:
                    f[j] = f[selected] + l
                    if not inLine[j]:
                        inLine[j] = True
                        toGo.append(j)
        result = 0
        for i in range(N):
            if f[i] <= M: result += 1
        for i, j, l in edges:
            tmp1 = max(M - f[i], 0)
            tmp2 = max(M - f[j], 0)
            result = result + min(l, tmp1 + tmp2)
        return result



s = Solution()
print(s.reachableNodes([[3,13,87],[14,15,96],[11,12,34],[5,16,28],[10,14,14],[9,16,98],[2,15,57],[6,17,55],[10,11,31],[13,16,80],[5,12,19],[16,17,67],[4,9,67],[2,10,94],[4,5,84],[3,17,44],[5,11,73],[17,18,51],[2,5,13],[7,9,54],[3,7,72],[0,10,93],[9,10,56],[15,16,26],[2,7,51],[10,12,70],[10,13,28],[12,19,13],[7,16,19],[4,10,30],[6,15,20],[1,8,29],[0,1,4],[0,18,44],[4,16,69],[3,8,1],[13,18,16],[7,15,10],[9,13,42],[9,12,88],[17,19,27],[8,12,40],[11,15,35],[10,15,15],[3,5,9],[4,17,21],[15,18,4],[6,18,39],[5,8,76],[1,13,28],[11,17,99],[7,19,50],[5,14,76],[6,8,57],[7,12,57],[8,18,78],[12,17,79],[7,13,20],[8,14,16],[16,18,18],[3,10,23],[8,16,7],[14,16,23],[2,3,40],[15,17,63],[4,8,2],[16,19,62],[9,19,71],[5,19,90],[13,14,66],[11,14,57],[5,7,30],[0,16,38],[1,2,61],[12,15,81],[7,17,35],[10,16,67],[11,18,36],[4,14,62],[1,5,4],[4,12,10],[3,12,66],[5,10,86],[1,19,31],[11,13,74],[0,7,77],[12,16,6],[5,18,67],[3,6,43],[14,17,20],[1,4,20],[18,19,82],[0,12,68],[6,12,40],[3,14,47],[1,10,16],[15,19,99],[11,16,53],[4,6,7],[4,18,41]], 73, 20))
print(s.reachableNodes([[0,1,10],[0,2,1],[1,2,2]], 6, 3))
print(s.reachableNodes([[0,1,4],[1,2,6],[0,2,8],[1,3,1]], 10, 4))

