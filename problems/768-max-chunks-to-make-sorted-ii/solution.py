#
# @lc app=leetcode id=768 lang=python3
#
# [768] Max Chunks To Make Sorted II
#
# https://leetcode.com/problems/max-chunks-to-make-sorted-ii/description/
#
# algorithms
# Hard (48.76%)
# Likes:    444
# Dislikes: 20
# Total Accepted:    21.6K
# Total Submissions: 44.3K
# Testcase Example:  '[5,4,3,2,1]'
#
# This question is the same as "Max Chunks to Make Sorted" except the integers
# of the given array are not necessarily distinct, the input array could be up
# to length 2000, and the elements could be up to 10**8.
# 
# 
# 
# Given an array arr of integers (not necessarily distinct), we split the array
# into some number of "chunks" (partitions), and individually sort each chunk.
# After concatenating them, the result equals the sorted array.
# 
# What is the most number of chunks we could have made?
# 
# Example 1:
# 
# 
# Input: arr = [5,4,3,2,1]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3],
# which isn't sorted.
# 
# 
# Example 2:
# 
# 
# Input: arr = [2,1,3,4,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [2, 1], [3, 4, 4].
# However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks
# possible.
# 
# 
# Note:
# 
# 
# arr will have length in range [1, 2000].
# arr[i] will be an integer in range [0, 10**8].
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    # O(N) solution
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ret, n, f, b = 1, len(arr), arr[:], arr[:]
        # f: forward array = max(arr[:i]), b: backward array: min(arr[i:])
        for i in range(1, n):
            f[i] = max(arr[i], f[i-1])
        for i in range(n-2, -1, -1):
            b[i] = min(arr[i], b[i+1])
        for i in range(n-1):
            if f[i] <= b[i+1]:
                ret += 1
        return ret
# @lc code=end
# O(Nlog N) Solutions       
"""
# sliding window
class Solution(object):
    def maxChunksToSorted(self, arr):
        count = collections.defaultdict(int)
        ans = nonzero = 0

        for x, y in zip(arr, sorted(arr))
            count[x] += 1
            if count[x] == 0: nonzero -= 1
            if count[x] == 1: nonzero += 1

            count[y] -= 1
            if count[y] == -1: nonzero += 1
            if count[y] == 0: nonzero -= 1

            if nonzero == 0: ans += 1

        return ans
'''
'''
# sorted count pairs

class Solution(object):
    def maxChunksToSorted(self, arr):
        count = collections.Counter()
        counted = []
        for x in arr:
            count[x] += 1
            counted.append((x, count[x]))

        ans, cur = 0, None
        for X, Y in zip(counted, sorted(counted)):
            cur = max(cur, X)
            if cur == Y:
                ans += 1
        return ans
        
""" 
