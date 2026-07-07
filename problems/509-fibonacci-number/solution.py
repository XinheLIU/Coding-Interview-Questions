#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        x, y = 1, 0
        if N == 0: return y
        for _ in range(1, N):
            x, y = x + y, x
        return x
        
# @lc code=end

