#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = [0] * 256
        for c in s:
            cnt[ord(c)] += 1
        for i, c in enumerate(s):
            if cnt[ord(c)] == 1:
                return i
        return -1        
# @lc code=end

