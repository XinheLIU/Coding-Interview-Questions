#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # decreasing stack
        s = collections.deque()
        ret = [0] * len(T)
        for i, v in enumerate(T):
            while s and T[s[-1]] < v:
                t = s.pop()
                ret[t] = i - t 
            s.append(i)
        return ret
# @lc code=end

