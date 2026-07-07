#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = float('inf')
        l, r = 0, 0
        window = collections.defaultdict(int)
        needs = collections.Counter(t)
        ret = ""
        match = 0
        while r < len(s):
            c1 = s[r]
            if needs[c1] > 0:
                window[c1] += 1
                if window[c1] == needs[c1]:
                    match += 1
            r += 1
            while match == len(needs):
                if r - l < min_len:
                    ret = s[l:r]
                    min_len = r - l
                c2 = s[l]
                if needs[c2] > 0:
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                l += 1
        return ret
# @lc code=end

