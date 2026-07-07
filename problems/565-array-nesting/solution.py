#
# @lc app=leetcode id=565 lang=python3
#
# [565] Array Nesting
#

# @lc code=start
import sys

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums)):
            if nums[i] != sys.maxsize:
                start = nums[i]
                cnt = 0
                while nums[start] < sys.maxsize:
                    nums[start], start = sys.maxsize, nums[start]
                    cnt += 1
                ret = max(cnt, ret)
        return ret
        
# @lc code=end

