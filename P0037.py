class Solution:
    result = []

    def calcCandidate(self, board):
        rows = []
        cols = []
        sqs = []
        for i in range(9):
            tmp = set(range(1, 10))
            for j in range(9):
                if board[i][j] != '.':
                    tmp.remove(ord(board[i][j]) - ord('0'))
            rows.append(tmp)
        for i in range(9):
            tmp = set(range(1, 10))
            for j in range(9):
                if board[j][i] != '.':
                    tmp.remove(ord(board[j][i]) - ord('0'))
            cols.append(tmp)
        for i in range(3):
            tmp1 = []
            for j in range(3):
                tmp = set(range(1, 10))
                for m in range(3):
                    for n in range(3):
                        if board[i * 3 + m][j * 3 + n] != '.':
                            tmp.remove(ord(board[i * 3 + m][j * 3 + n]) - ord('0'))
                tmp1.append(tmp)
            sqs.append(tmp1)
        return rows, cols, sqs

    def calcSingleCand(self, x, y, rows, cols, sqs):
        return rows[x] & cols[y] & sqs[x // 3][y // 3]

    def getCurrentGuess(self, board, rows, cols, sqs):
        x = y = -1
        candList = []
        minNum = 10
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    cand = self.calcSingleCand(i, j, rows, cols, sqs)
                    if len(cand) == 0:
                        return -2, -2, []
                    elif len(cand) < minNum:
                        minNum = len(cand)
                        x = i
                        y = j
                        candList = cand
        return x, y, candList


    def dfs(self, board, rows, cols, sqs):
        x, y, candList = self.getCurrentGuess(board, rows, cols, sqs)
        if x == y == -1:
            return 1
        for cand in candList:
            board[x][y] = chr(cand + ord('0'))
            rows[x].remove(cand)
            cols[y].remove(cand)
            sqs[x // 3][y // 3].remove(cand)
            if self.dfs(board, rows, cols, sqs) == 1:
                return 1
            board[x][y] = '.'
            rows[x].add(cand)
            cols[y].add(cand)
            sqs[x // 3][y // 3].add(cand)

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.result = board
        rows, cols, sqs = self.calcCandidate(board)
        self.dfs(board, rows, cols, sqs)


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

s = Solution()
s.solveSudoku(board)
print(board)
