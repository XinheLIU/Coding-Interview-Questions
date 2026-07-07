#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from collections import Counter, defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ret = []
        window, needs = defaultdict(int), Counter(p)
        l, r = 0, 0
        match = 0
        while r < len(s):
            c1 = s[r]
            window[c1] += 1
            if needs[c1] == window[c1]:
                match += 1
            r += 1
            while match == len(needs):
                if r - l == len(p):
                    ret.append(l)
                c2 = s[l]
                if needs[c2] > 0:
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                l += 1
        return ret
# @lc code=end

