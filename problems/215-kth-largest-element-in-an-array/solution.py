#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (50.46%)
# Likes:    2928
# Dislikes: 208
# Total Accepted:    522.6K
# Total Submissions: 999.9K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k < 1 or k > len(nums):
            return None
        l, r, n = 0, len(nums) - 1, len(nums)
        while l <= r:
            pivot_pos = self.partition(nums, l, r)
            if pivot_pos == n - k:
                return nums[pivot_pos]
            elif pivot_pos < n - k:
                l = pivot_pos + 1
            else:
                r = pivot_pos - 1
                
    # quick sort
    def partition(self, nums, l, r):
        """
        make sure start <= k <= end
        compare the pivots position with k
        whether to repeat again 
        """
        i, pivot = l - 1, nums[r]
        for j in range(l,r):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[r] = nums[r], nums[i+1]
        return i + 1 
# @lc code=end

