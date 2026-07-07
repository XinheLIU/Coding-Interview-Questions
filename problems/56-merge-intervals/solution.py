#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        ret = []
        for interval in intervals:
            if not ret or ret[-1][-1] < interval[0]:
                ret.append(interval)
            else:
                ret[-1][-1] = max(interval[-1], ret[-1][-1])
        return ret
# @lc code=end

