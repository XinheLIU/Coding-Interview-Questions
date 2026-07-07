#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret, cnt = 0, 0
        for v in nums:
            if v == 1:
                cnt += 1
                ret = max(ret, cnt)
            else:
                cnt = 0
        return ret
# @lc code=end

