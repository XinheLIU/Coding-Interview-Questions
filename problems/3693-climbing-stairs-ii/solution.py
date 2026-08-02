#
# @lc app=leetcode id=3693 lang=python3
#
# [3693] Climbing Stairs II
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # Climbing Stairs with cost and step constraints
        # Can climb 1, 2, or 3 steps at a time, each with a cost
        # State: dp[i] = minimum cost to reach step i
        # Transition: dp[i] = min(dp[i-1]+cost[i-1]*1, dp[i-2]+cost[i-2]*4, dp[i-3]+cost[i-3]*9) + costs[i]
        #
        # Space-optimized: rolling three variables (x, y, z) = (i-3, i-2, i-1)
        # Cost multipliers: 1 step costs 1x, 2 steps costs 4x, 3 steps costs 9x
        x = y = z = 0  # base: cost to reach positions before the start
        for c in costs:
            # Update: new position = min of (3-step-back + 9*cost, 2-step-back + 4*cost, 1-step-back + 1*cost) + current cost
            x, y, z = y, z, min(x + 9, y + 4, z + 1) + c
        return z  # z now holds the cost to reach the final step
# @lc code=end

