class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            d = set()
            for j in range(9):
                if board[i][j] in d:
                    return False
                else:
                    if board[i][j] != '.':
                        d.add(board[i][j])

        for i in range(9):
            d = set()
            for j in range(9):
                if board[j][i] in d:
                    return False
                else:
                    if board[j][i] != '.':
                        d.add(board[j][i])

        for i in range(3):
            for j in range(3):
                d = set()
                for m in range(3):
                    for n in range(3):
                        if board[i * 3 + m][j * 3 + n] in d:
                            return False
                        else:
                            if board[i * 3 + m][j * 3 + n] != '.':
                                d.add(board[i * 3 + m][j * 3 + n])

        return True


board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

s = Solution()
print(s.isValidSudoku(board))
