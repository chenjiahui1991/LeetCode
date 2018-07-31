class Solution:
    def getNext(self, board, visited):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '1' and visited[i][j] == False:
                    return (i, j)
        return None

    def numIslands(self, board):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(board) == 0 or len(board[0]) == 0:
            return 0
        result = 0
        step = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        now = self.getNext(board, visited)
        while now is not None:
            line = [now]
            visited[now[0]][now[1]] = True
            point, right = 0, 0
            while point <= right:
                x, y = line[point]
                if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                    flag = False
                for i in range(4):
                    newx, newy = x + step[i][0], y + step[i][1]
                    if 0 <= newx < m and 0 <= newy < n and visited[newx][newy] == False and board[newx][newy] == '1':
                        line.append((newx, newy))
                        visited[newx][newy] = True
                        right += 1
                point += 1
            result += 1
            now = self.getNext(board, visited)
        return result


s = Solution()
# board = ['11110',
#          '11010',
#          '11000',
#          '00000']
board = [
    '11000',
    '11000',
    '00100',
    '00011'
]
print(s.numIslands(board))
