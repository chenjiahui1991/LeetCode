class Solution:
    def dfs(self, word, board, visited, x, y):
        if word == '':
            return True
        step = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(4):
            xx = x + step[i][0]
            yy = y + step[i][1]
            if board[xx][yy] == word[0] and visited[xx][yy] == False:
                visited[xx][yy] = True
                if self.dfs(word[1 :], board, visited, xx, yy):
                    return True
                visited[xx][yy] = False
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0:
            return False
        tmp = [['$' for _ in range(n + 2)]]
        for i in range(m):
            tmp.append(['$'] + board[i] + ['$'])
        tmp.append(['$' for _ in range(n + 2)])
        board = tmp
        tmp = [[True for _ in range(n + 2)]]
        for i in range(m):
            tmp.append([True] + [False for _ in range(n)] + [True])
        tmp.append([True for _ in range(n + 2)])
        visited = tmp
        m += 2
        n += 2
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if self.dfs(word[1:], board, visited, i, j):
                        return True
                    visited[i][j] = False
        return False


s = Solution()
board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(s.exist(board, "ABCCED"))
print(s.exist(board, "SEE"))
print(s.exist(board, "ABCB"))
