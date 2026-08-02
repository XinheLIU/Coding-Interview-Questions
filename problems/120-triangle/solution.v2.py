#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# Approach 2: In-place DP modifying the input triangle

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Same bottom-up DP but modify the triangle in-place
        # dp[i][j] = minimum path sum from (i,j) to bottom
        # Space: O(1) if we're allowed to modify input, O(n) if not
        dp = triangle
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
        return dp[0][0]
# @lc code=end
