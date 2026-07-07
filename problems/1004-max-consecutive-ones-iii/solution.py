#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], K: int) -> int:
        ret = 0
        zeros = 0
        left = 0
        for right, v in enumerate(nums):
            if v == 0:
                zeros += 1
            while zeros > K:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            ret = max(ret, right - left + 1)
        return ret
# @lc code=end

