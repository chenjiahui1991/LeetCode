class Solution:
    def getNext(self, board, visited):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and visited[i][j] == False:
                    return (i, j)
        return None

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0 or len(board[0]) == 0:
            return
        step = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        now = self.getNext(board, visited)
        while now is not None:
            line = [now]
            visited[now[0]][now[1]] = True
            point, right = 0, 0
            flag = True
            while point <= right:
                x, y = line[point]
                if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                    flag = False
                for i in range(4):
                    newx, newy = x + step[i][0], y + step[i][1]
                    if 0 <= newx < m and 0 <= newy < n and visited[newx][newy] == False and board[newx][newy] == 'O':
                        line.append((newx, newy))
                        visited[newx][newy] = True
                        right += 1
                point += 1
            if flag:
                for pos in line:
                    board[pos[0]][pos[1]] = 'X'
            now = self.getNext(board, visited)


s = Solution()
board = [['X', 'X', 'X', 'X'],
         ['X', 'O', 'O', 'X'],
         ['X', 'X', 'O', 'X'],
         ['X', 'O', 'X', 'X']]
s.solve(board)
print(board)
