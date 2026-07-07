#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        N = len(s)
        res = ""
        pos = 0
        while pos < N:
            nx = s[pos : pos + k]
            res = res + nx[::-1] + s[pos + k : pos + 2 * k]
            pos += 2 * k
        return res
# @lc code=end
'''
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return ''.join(s[i:i+k][::-1] + s[i+k:i+2*k] for i in range(0, len(s), 2*k))
'''

