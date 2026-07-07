#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n):
            sum = nums[i]
            for j in range(i + 1, n):
                sum += nums[j]
                if sum == k:
                    return True
                elif k != 0 and sum % k == 0:
                    return True
        return False
# @lc code=end

