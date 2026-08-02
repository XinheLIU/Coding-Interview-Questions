#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Bottom-up DP with space optimization: reuse the last row as the DP array
        # State: dp[j] = minimum path sum from bottom to position (i, j)
        # Transition: dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        #   (each cell can only reach the two cells directly below it)
        #
        # Why bottom-up? Starting from the bottom means each cell has exactly 2 choices,
        # whereas top-down would require tracking multiple paths converging at each cell.
        dp, n = triangle[-1], len(triangle)

        # Work backwards from second-to-last row to the top
        for i in range(n-2, -1, -1):
            for j in range(len(triangle[i])):
                # Take the minimum of the two possible next steps, add current cost
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]

        return dp[0]  # Answer is at the top of the triangle
# @lc code=end