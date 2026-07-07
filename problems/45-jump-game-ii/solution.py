#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        canReach = 0
        cnt = 0
        pos = 0
        while canReach < n-1:
            cnt += 1
            preReach = canReach
            while pos <= preReach:
                canReach = max(canReach, pos + nums[pos])
                pos += 1
        return cnt
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if nums.count(1)== n:return n-1
        pos = len(nums) - 1
        steps = 0
        # backwards
        while pos != 0:
            for i, jump in enumerate(nums):
                if pos - jump <= i:
                    pos = i
                    steps += 1
                    break
        return steps
'''
# @lc code=end

