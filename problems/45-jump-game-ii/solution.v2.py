#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        cur_reachable = 0
        i = 0
        steps = 0
        while cur_reachable < n - 1:
            steps += 1
            pre_reachable = cur_reachable
            while i <= pre_reachable:
                cur_reachable = max(i + nums[i], cur_reachable)
                i += 1
            if pre_reachable == cur_reachable: # no further jump
                return -1
        return steps
# @lc code=end

