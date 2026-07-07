#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
from itertools import combinations
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        def dfs(num, hours, ret):
            if hours > num:
                return
            for hour in combinations([1,2,4,8], hours):
                hs = sum(hour)
                if hs >= 12: continue
                for minu in combinations([1,2,4,8,16,32], num - hours):
                    mins = sum(minu)
                    if mins >= 60: continue
                    ret.append("%d:%02d" % (hs, mins))
            dfs(num, hours + 1, ret)
        ret = []
        dfs(num, 0, ret)
        return ret
# @lc code=end

