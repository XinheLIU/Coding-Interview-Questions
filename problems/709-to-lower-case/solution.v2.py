#
# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
#

# @lc code=start
class Solution:
    def toLowerCase(self, str: str) -> str:
        # | 32 to lower case , & 32 to higher case, ^ high to low, low to high
        return ''.join(map(lambda x: chr(ord(x) | 32), list(str)))
# @lc code=end

