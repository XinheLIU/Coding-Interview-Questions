#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        # could also use set for diff and sum
        self.DFS(n, [], [], [])
        return self.res
        
    def DFS(self, n, queens, xy_diff, xy_sum):
        p = len(queens) # col pos in every row
        if p == n:
            self.res += 1
            return
        for q in range(n):
            if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                self.DFS(n, queens + [q], xy_diff + [p-q], xy_sum + [p+q])
                
'''
# bitwise solution

class Solution:
    # bitwise solution
    def totalNQueens(self, n):
        self.count = 0
        # could also use set for diff and sum
        self.DFS(n, 0, 0, 0, 0)
        return self.count
        
    def DFS(self, n, row, col, l, r): # l = "pie", r = "na"
        if row >= n:
            self.count += 1
            return 
        # all positions can be tried as 1
        bits = (~(col | l | r)) & ((1 << n) - 1) # n 1s 
        
        while bits:
            p = bits & -bits # get lowest 1
            self.DFS(n, row + 1, col| p, (l | p) << 1, (r | p) >> 1)
            bits &= (bits - 1) # get rid of lowest 1
'''
# @lc code=end

