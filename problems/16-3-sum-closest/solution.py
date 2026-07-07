#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = sum(nums[:3])
        mindiff = abs(closest - target)
        for i in range(0, len(nums)-2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                Sum = nums[i] + nums[l] + nums[r]
                diff = abs(Sum - target)
                if diff < mindiff:
                    mindiff = diff
                    closest = Sum
                if Sum < target:
                    l += 1
                else:
                    r -= 1
        return closest
# @lc code=end

