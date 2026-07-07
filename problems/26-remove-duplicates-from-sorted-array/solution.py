#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 # slow pointer
        for v in nums:
            if nums[i] != v:
                i += 1
                nums[i] = v
        return i + 1
# @lc code=end

