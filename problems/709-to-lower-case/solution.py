#
# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
#

# @lc code=start
class Solution:
    def toLowerCase(self, str: str) -> str:
        ret = ''
        for c in str:
            ret += chr(ord(c) | 32)
        return ret
# @lc code=end