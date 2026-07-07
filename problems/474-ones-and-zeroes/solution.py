#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        #dp[i][j] is the maximum number we find with i zeros and j ones
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for s in strs:
            zeros = sum([1 if c == "0" else 0 for c in s])
            ones = sum([1 if c == "1" else 0 for c in s])
            for i in range(m, zeros -1, -1):
                for j in range(n, ones -1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[m][n]
# @lc code=end

