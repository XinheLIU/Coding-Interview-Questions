#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ret = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], "."}
                    if j + 1 < len(p) and p[j+1] == "*":
                        ret = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ret = first_match and dp(i+1, j+1)
                memo[i,j] = ret
            return memo[i, j]
        return dp(0, 0)
# @lc code=end

