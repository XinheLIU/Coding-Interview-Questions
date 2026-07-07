#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i,j] is to match s[:i] and t[:j] (start from empty string)
        n1, n2 = len(s), len(t)
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for i in range(n1 + 1): # to math an empty string ""
            dp[i][0] = 1
        for i in range(1, n1 + 1):
            for j in range(1, n2+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n1][n2]
# @lc code=end

