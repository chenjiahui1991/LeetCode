# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None:
            return None
        reset = set()
        reset.add(node.label)
        visited = set()
        visited.add(node.label)
        result = UndirectedGraphNode(node.label)
        mem = dict()
        mem[node.label] = result

        def dfs(node, visited, reset, mem):
            for nei in node.neighbors:
                if nei.label not in reset:
                    reset.add(nei.label)
                    tmp = UndirectedGraphNode(nei.label)
                    mem[nei.label] = tmp
                mem[node.label].neighbors.append(mem[nei.label])
                if nei.label not in visited:
                    visited.add(nei.label)
                    dfs(nei, visited, reset, mem)

        dfs(node, visited, reset, mem)

        for label in mem:
            print(label, mem[label].neighbors)
        return result



s = Solution()
tmp0 = UndirectedGraphNode(0)
tmp1 = UndirectedGraphNode(1)
tmp2 = UndirectedGraphNode(2)
tmp0.neighbors = [tmp1, tmp2]
tmp1.neighbors = [tmp2]
tmp2.neighbors = [tmp2]

s.cloneGraph(tmp0)
