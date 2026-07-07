class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        R, C = len(board), len(board[0])
        todo = False
        
        '''
        If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all         at the same time - these positions become empty.
        '''

        for r in range(R):
            for c in range(C-2):
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                    board[r][c] = board[r][c+1] = board[r][c+2] = -abs(board[r][c])
                    todo = True

        for r in range(R-2):
            for c in range(C):
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])
                    todo = True

        '''
        After crushing all candies simultaneously, if an empty space on the board has candies on top of           itself, then these candies will drop until they hit a candy or bottom at the same time. (No new           candies will drop outside the top boundary.)
        '''
        for c in range(C):
            wr = R-1
            for r in range(R-1, -1, -1):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for wr in range(wr, -1, -1):
                board[wr][c] = 0
        '''
        After the above steps, there may exist more candies that can be crushed. If so, you need to                 repeat the above steps.
        '''
        return self.candyCrush(board) if todo else board