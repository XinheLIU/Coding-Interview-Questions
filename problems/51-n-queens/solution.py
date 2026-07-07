#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:   
        def dfs(n, ret, queens, xy_sum, xy_diff):
            x = len(queens)
            if x == n:
                ret.append(queens)
                return 
            for y in range(n):
                if y not in queens and (x-y) not in xy_diff and (x+y) not in xy_sum:
                    dfs(n, ret, queens + [y], xy_sum + [x+y], xy_diff + [x-y])
        ret = []
        dfs(n, ret, [], [], [])
        return [['.' * i + 'Q' + (n-i-1) * '.' for i in sol] for sol in ret]

'''
class Solution:
    # diagonal : x+ y = c (y = -x + c) or x - y = c (y = x - c)                
    def solveNQueens(self, n):
        ret = []
        self.DFS(n, ret, [], set(), set())
        return [["." * i + "Q" + "." *(n-i-1) for i in sol] for sol in ret ]
    
    def DFS(self, n, ret, queens, xy_diff, xy_sum):
        x = len(queens) # col pos in every row
        if x == n:
            ret.append(queens)
            return
        for y in range(n):
            if y not in queens and x-y not in xy_diff and x+y not in xy_sum:
                xy_diff.add(x-y)
                xy_sum.add(x+y)
                self.DFS(n, ret, queens + [y], xy_diff, xy_sum)     
                xy_diff.remove(x-y)
                xy_sum.remove(x+y) 
'''  
# @lc code=end

