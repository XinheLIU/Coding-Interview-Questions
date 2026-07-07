#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1
        while end >= 0 and s[end].isspace():
            end -= 1
        if end < 0: 
            return 0
        start = end
        while start >= 0 and not s[start].isspace():
            start -= 1
        return end - start
# @lc code=end

