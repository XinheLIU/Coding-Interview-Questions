#
# @lc app=leetcode id=436 lang=python3
#
# [436] Find Right Interval
#

# @lc code=start
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
		ns = sorted([(d[0], i) for i, d in enumerate(intervals)]) # order and index
        ret = []
        for d in intervals:
            n = d[1]
            if n > ns[-1][0]:
                ret.append(-1)
            elif n <= ns[0][0]:
                ret.append(ns[0][1])
            else:
                l, r = 0, len(ns) - 1
                while l + 1 < r:
                    mid = (l + r) >> 1
                    if ns[mid][0] >= n:
                        r = mid
                    else:
                        l = mid
                ret.append(ns[r][1])
        return ret
# @lc code=end

