#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needs = collections.Counter(s1)
        window = collections.defaultdict(int)
        l, r = 0, 0
        match = 0
        while r < len(s2):
            c1 = s2[r]
            if needs[c1] > 0:
                window[c1] += 1
                if window[c1] == needs[c1]:
                    match += 1
            r += 1
            while match == len(needs):
                if r - l == len(s1):
                    return True
                c2 = s2[l]
                if needs[c2] > 0:
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                l += 1
        return False
        
# @lc code=end

