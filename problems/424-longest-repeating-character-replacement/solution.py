#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        l, r = 0, 0
        max_count = 0
        ret = 0
        while r < len(s):
            c1 = s[r]
            count[c1] += 1
            max_count = max(max_count, count[c1])
            # flip char other than max_count
            while r - l + 1 - max_count > k:
                c2 = s[l]
                count[c2] -= 1
                max_count = max(max_count, count[c2])
                l += 1
            ret = max(ret, r - l + 1)
            r += 1
        return ret
        
# @lc code=end

