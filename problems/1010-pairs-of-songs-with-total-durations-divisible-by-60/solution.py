#
# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#

# @lc code=start
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = [0] * 60
        ret = 0
        # count
        for t in time:
            cnt[t % 60] += 1
        for i in range(31): 
            if i == 0 or i == 30:
                n = cnt[i]
                ret += n * (n-1) // 2 # combination C(n,2)
            else:
                ret += cnt[i] * cnt[60 - i] # pick two
        return ret
# @lc code=end

