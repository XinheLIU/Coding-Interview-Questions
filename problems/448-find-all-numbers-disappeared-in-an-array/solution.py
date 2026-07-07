#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for v in nums:
            if nums[abs(v) - 1] > 0:
                nums[abs(v) - 1] *= -1
        ret = []
        for i, v in enumerate(nums):
            if v > 0:
                ret.append(i + 1)
        return ret
# @lc code=end

