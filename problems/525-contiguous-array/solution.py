#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        m = dict()
        m[0] = -1
        ret = 0
        cnt = 0 # relative number of 0 and 1
        for i in range(len(nums)):
            cnt = cnt + (1 if nums[i] == 1 else -1)
            if cnt in m:
                ret = max(ret, i - m[cnt])
            else:
                m[cnt] = i
        return ret
        
# @lc code=end

