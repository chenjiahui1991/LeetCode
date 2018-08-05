class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = {}
        for word in words:
            t = trie
            for ch in word:
                if ch not in t:
                    t[ch] = {}
                t = t[ch]
            t['#'] = word
        result = []
        if len(board) == 0 or len(board[0]) == 0: return []
        m, n = len(board), len(board[0])

        step = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(board, visited, trie, x, y):
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] not in trie or visited[x][y]:
                return
            if '#' in trie[board[x][y]] and trie[board[x][y]]['#'] not in result: result.append(trie[board[x][y]]['#'])
            visited[x][y] = True
            for i in range(4):
                dfs(board, visited, trie[board[x][y]], x + step[i][0], y + step[i][1])
            visited[x][y] = False

        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dfs(board, visited, trie, i, j)
        return result

s = Solution()
board =[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
print(s.findWords(board, ["oath","pea","eat","rain"]))
print(s.findWords([['a']], ["a","a"]))
