#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#
# https://leetcode.com/problems/find-k-closest-elements/description/
#
# algorithms
# Medium (40.92%)
# Likes:    1508
# Dislikes: 261
# Total Accepted:    113.9K
# Total Submissions: 277.7K
# Testcase Example:  '[1,2,3,4,5]\n4\n3'
#
# Given a sorted array arr, two integers k and x, find the k closest elements
# to x in the array. The result should also be sorted in ascending order. If
# there is a tie, the smaller elements are always preferred.
# 
# 
# Example 1:
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:
# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]
# 
# 
# Constraints:
# 
# 
# 1 <= k <= arr.length
# 1 <= arr.length <= 10^4
# Absolute value of elements in the array and x will not exceed 10^4
# 
# 
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        # left most bound
        while l < r:
            mid = l + ((r - l) >> 1)
            if  x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
        return arr[l:l + k] 
# @lc code=end

