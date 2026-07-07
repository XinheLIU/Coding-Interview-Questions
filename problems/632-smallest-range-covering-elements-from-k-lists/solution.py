#
# @lc app=leetcode id=632 lang=python3
#
# [632] Smallest Range Covering Elements from K Lists
#
# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/
#
# algorithms
# Hard (52.53%)
# Likes:    1112
# Dislikes: 25
# Total Accepted:    39.1K
# Total Submissions: 74.4K
# Testcase Example:  '[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]'
#
# You have k lists of sorted integers in ascending order. Find the smallest
# range that includes at least one number from each of the k lists.
# 
# We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c
# if b-a == d-c.
# 
# 
# 
# Example 1:
# 
# 
# Input: [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# Output: [20,24]
# Explanation: 
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
# 
# 
# 
# 
# Note:
# 
# 
# The given list may contain duplicates, so ascending order means >= here.
# 1 <= k <= 3500
# -10^5 <= value of elements <= 10^5.
# 
# 
#

# @lc code=start
import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap, n, maxv = [], len(nums), float('-inf')
        for i in range(n):
            # add the fist element to heap
            if len(nums[i]):
                heap.append((nums[i][0], i, 0))
                maxv = max(maxv, nums[i][0])
            heapq.heapify(heap)
            ret = [float('-inf'), maxv]
            while len(heap) == n:
                minv, index_a, index_i = heapq.heappop(heap)
                # update ret
                if maxv - minv < ret[1] - ret[0]:
                    ret = [minv, maxv]
                # insert next element
                if index_i + 1 < len(nums[index_a]):
                    maxv = max(nums[index_a][index_i + 1], maxv)
                    heapq.heappush(heap, (nums[index_a][index_i + 1], index_a, index_i + 1))
        return ret
# @lc code=end

