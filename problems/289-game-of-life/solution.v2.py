class Solution:

    def liveNeighbors(self, board, m, n, i, j):
        lives = 0
        for x in range(max(i - 1, 0), min(i + 1, m - 1) + 1):
            for y in range(max(j - 1, 0), min(j + 1, n - 1) + 1):
                lives += board[x][y] & 1
        lives -= board[i][j] & 1
        return lives

    def gameOfLife(self, board):
        """
        state
        0 dead to dead
        1 live to live
        2 live to dead
        3 dead to live
        """
        # Write your code here
        m = len(board)
        n = len(board[0])
    
        for i in range(m):
            for j in range(n):
                lives = self.liveNeighbors(board, m, n, i, j)
                if board[i][j] == 1 and 3 >= lives >= 2:  
                    board[i][j] = 3
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1