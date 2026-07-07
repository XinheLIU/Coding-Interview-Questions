#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sumv = sum(nums[:k])
        maxv = sumv
        for i in range(k, len(nums)):
            sumv += (nums[i] - nums[i - k])
            maxv = max(maxv, sumv)
        return maxv / k
# @lc code=end

