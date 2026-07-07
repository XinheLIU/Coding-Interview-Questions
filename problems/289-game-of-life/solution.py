#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
    def liveNeighbors(self, board, m, n, i, j):
        lives = 0
        for x in range(max(i - 1, 0), min(i + 1, m - 1) + 1):
            for y in range(max(j - 1, 0), min(j + 1, n - 1) + 1):
                lives += board[x][y] & 1
        lives -= board[i][j] & 1
        return lives

    def gameOfLife(self, board):
        # Write your code here
        m = len(board)
        n = len(board[0])
    
        for i in range(m):
            for j in range(n):
                lives = self.liveNeighbors(board, m, n, i, j)
                # Any live cell with fewer than two live neighbors dies, as if caused by under-population.
                # Any live cell with two or three live neighbors lives on to the next generation.
                # Any live cell with more than three live neighbors dies, as if by over-population..
               #  Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction. 
                if board[i][j] == 1 and 3 >= lives >= 2:  
                    board[i][j] = 3
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 2
        # update cell status
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
# @lc code=end

