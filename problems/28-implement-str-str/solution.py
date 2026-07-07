#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if not n: return 0
        if m < n: return -1
        for i in range(m-n+1):
            if haystack[i: i + n] == needle:
                return i
        return -1
# @lc code=end

