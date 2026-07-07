#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#

# @lc code=start
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        ret = 0
        m = float('inf')
        sorted_l = sorted(range(len(A)), key = A.__getitem__)
        for i in sorted_l:
            ret = max(ret, i - m)
            m = min(m, i)
        return ret
# @lc code=end

