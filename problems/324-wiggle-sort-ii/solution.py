#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#
# https://leetcode.com/problems/wiggle-sort-ii/description/
#
# algorithms
# Medium (29.95%)
# Likes:    1129
# Dislikes: 579
# Total Accepted:    86.8K
# Total Submissions: 288K
# Testcase Example:  '[1,5,1,1,6,4]'
#
# Given an unsorted array nums, reorder it such that nums[0] < nums[1] >
# nums[2] < nums[3]....
# 
# Example 1:
# 
# 
# Input: nums = [1, 5, 1, 1, 6, 4]
# Output: One possible answer is [1, 4, 1, 5, 1, 6].
# 
# Example 2:
# 
# 
# Input: nums = [1, 3, 2, 2, 3, 1]
# Output: One possible answer is [2, 3, 1, 3, 1, 2].
# 
# Note:
# You may assume all input has valid answer.
# 
# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        # partition nums into smaller half and bigger half
        # all nums in smaller half <= any num in bigger half
        median = self.find_median(nums)
        
        n = len(nums)

        # reorder the nums from
        # 0 => n-1(odd), (n-2)(even)
        # 1 => n-3
        # 2 => n-5
        # ...
        # (n - 1) / 2 => 0
        # (n - 1) / 2 + 1 => n - 2(odd), n - 1(even)
        # (n - 1) / 2 + 2 => n - 4(odd), n - 3(even)
        # ... 
        def get_index(i):
            if i <= (n - 1) // 2:
                return n - i * 2 - 1 - (n + 1) % 2
            i -= (n - 1) // 2 + 1
            return n - i * 2 - 1 - n % 2
            
        # 3-way partition
        left, i, right = 0, 0, n - 1
        while i <= right:
            if nums[get_index(i)] < median:
                nums[get_index(left)], nums[get_index(i)] = nums[get_index(i)], nums[get_index(left)]
                i += 1
                left += 1
            elif nums[get_index(i)] == median:
                i += 1
            else:
                nums[get_index(right)], nums[get_index(i)] = nums[get_index(i)], nums[get_index(right)]
                right -= 1
        
    def find_median(self, nums):
        return self.find_kth(nums, 0, len(nums) - 1, (len(nums) - 1) // 2)
    
    def find_kth(self, nums, start, end, kth):
        # k is zero based
        left, right = start, end
        mid = nums[(left + right) // 2]
        
        while left <= right:
            while left <= right and nums[left] < mid:
                left += 1
            while left <= right and nums[right] > mid:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
                
        if kth <= right:
            return self.find_kth(nums, start, right, kth)
        elif kth >= left:
            return self.find_kth(nums, left, end, kth)
        else:
            return nums[kth]
        
# @lc code=end
'''
def wiggleSort(self, nums):
    nums.sort()
    half = len(nums[::2])
    nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
'''
