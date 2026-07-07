#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return []
        m = len(board)
        if not m:
            return False
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, visited, i, j):
                    return True
        return False

    def dfs(self, board, word, visited, row, col):
        if not word:
            return True
        m, n = len(board), len(board[0])
        if 0 <= row < m and 0 <= col < n:
            if board[row][col] == word[0] and not visited[row][col]:
                visited[row][col] = True
                if self.dfs(board, word[1:], visited, row + 1, col) or \
                   self.dfs(board, word[1:], visited, row - 1, col) or \
                   self.dfs(board, word[1:], visited, row, col + 1) or \
                   self.dfs(board, word[1:], visited, row, col - 1):
                    return True
                else:
                    visited[row][col] = False
        return False
# @lc code=end

