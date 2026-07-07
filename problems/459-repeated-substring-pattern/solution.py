#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(n // 2, 0, -1):
            if n % i == 0:
                l = n // i
                if s[:i] * l == s:
                    return True
        return False
# @lc code=end

