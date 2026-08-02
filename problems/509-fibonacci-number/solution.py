#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        # Space-optimized DP: O(1) space instead of O(n) table
        # The recurrence dp[i] = dp[i-1] + dp[i-2] only looks back 2 states,
        # so we can collapse the table into two rolling variables.
        x, y = 1, 0  # x = fib(1), y = fib(0)
        if N == 0: return y

        for _ in range(1, N):
            # Move the window: compute next fib, shift both pointers
            x, y = x + y, x
        return x

# @lc code=end

